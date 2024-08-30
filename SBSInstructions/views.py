import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth import login

from SBSInstructions.form import SignupForm, EmailAuthenticationForm, AnleitungForm, AnleitungsschrittForm, KomponenteForm, SchrittundKomponentenMultiForm
from SBSInstructions.models import Profil, Anleitung, Anleitungsschritt, Komponente


# Create your views here.

class StartseiteListView(ListView):

    #  Definierung des Models das verwendet wird
    model = Anleitung

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Startseite.html'
    
    # Holen der Daten aus der Datenbank und werden in den Kontext, der zur HTML und Javascript geschickt wird, gepackt
    def get_object(self):
        return Anleitung.objects.all()

    def get_context_data(self, **kwargs):

        # Holt die Anleitung
        context = super().get_context_data(**kwargs)

        # Kontextdaten setzen
        context = { 'anleitung': list(Anleitung.objects.values('profil', 'anleittitel', 'kategorie', 'dauer', 'datum', 'img'))}

        return context



# Anleitung wurde erstellt
def anleitunggespeichert(request):
    return render(request, 'Anleitunggespeichert.html')

# Anleitung wurde durchgegangen
def anleitungfertig(request):
    return render(request, 'Anleitungfertig.html')

# Anleitung wurde teilweise erstellt
def entwurffertig(request):
    return render(request, 'Entwurfgespeichert.html')



# erste Seite von Anleitungen wird hiermit erstellt
class AnleitungerstellenCreateView(CreateView):

    # Formular um die Daten aufzunehmen und Abzuspeichern
    form_class = AnleitungForm

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Anleitungerstellen.html'

    success_url = 'anleitungsschritteerstellen'

    # Falls der Benutzer eingelogt ist soll der Ersteller automatisch ausgefuellt werden
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # ersteller = None

        # if self.request.user.is_authenticated:
        #     ersteller = self.request.user.profil.ersteller

        # kwargs['ersteller'] = ersteller
        kwargs['initial'] = {'datum': datetime.date.today()}
        return kwargs

    
    # Daten werden im Formular gespeichert und zur datenbank geschickt
    def form_valid(self, form):        
        form.instance.datum = datetime.date.today()
        return super().form_valid(form)

class AnleitungsschritterstellenCreateView(CreateView):

    template_name = 'Anleitungsschritterstellen.html'

    form_class = AnleitungsschrittForm

    success_url = 'komponentenerstellen'

    def form_valid(self, form):
        anleitung = Anleitung.objects.latest('id')
        form.save_with_anleitung_id(anleitung)
        return super().form_valid(form)

class KomponentenerstellenCreateView(CreateView):
    template_name = 'Komponentenerstellen.html'
    form_class = KomponenteForm
    success_url = 'anleitungsschritteerstellen'

    def form_valid(self, form):
        anleitungsschritt = Anleitungsschritt.objects.latest('id')
        form.save_with_anleitungsschritt_id(anleitungsschritt)
        return super().form_valid(form)

    def get_success_url(self):
        if 'neueKomponente' in self.request.POST:
            return 'komponentenerstellen'
        elif 'neuerSchritt' in self.request.POST:    
            return 'anleitungsschritteerstellen'


# Anleitungen koennen hier durchgegangen werden
class AnleitungdurchgehenDetailView(DetailView):

    #  Definierung des Models das verwendet wird
    model = Anleitung

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Anleitungdurchgehen.html'
    
    # Holen der Daten aus der Datenbank und werden in den Kontext, der zur HTML und Javascript geschickt wird, gepackt
    def get_context_data(self, **kwargs):

        # Holt die Anleitung
        anleitung = self.get_object()

        # Kontextdaten setzen
        context = { 'anleitungstitel': anleitung,
                    'einzelschritte': list(Anleitungsschritt.objects.filter
                                           (anleitung = anleitung).values('id','schrittbenennung', 'beschreibung', 'schrittbild')),
                    'komponenten': list(Komponente.objects.values())}

        return context



# Erstellung des Profils
class ProfilerstellenCreateView(CreateView):

    model = Profil
    
    form_class = SignupForm
    
    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Profilerstellen.html'

    success_url = ('profileigeneanleitungen/' + str(Profil.objects.latest('id').id+1))
    

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# Einloggen
class ProfileinloggenLoginView(LoginView):

    template_name = 'Profileinloggen.html'
    authentication_form = EmailAuthenticationForm

    success_url = ('profileigeneanleitungen/' + str(Profil.objects.latest('id').id + 1))

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

# Eigeloggt und nur die selbst erstellten Entwuerfe und Anleitungen werden angezeigt
class ProfileigeneAnleitungenDetailView(DetailView):

    model = Profil
    template_name = 'ProfileigeneAnleitungen.html'

    def get_context_data(self, **kwargs):

        # Holt die Anleitung
        profil = self.get_object()

        # Kontextdaten setzen
        context = { 'profil': list(Profil.objects.values('id', 'benutzername')),
                    'anleitungen': list(Anleitung.objects.filter
                                           (profil = profil).values('id','anleittitel', 'kategorie', 'dauer', 'datum', 'img'))}

        return context



# Anleitungsschritt und Komponenten werden in einem Schritt aufgenommen. Funktioniert noch nicht
# Anleitungsschritte werden erstellt
# class AnleitungsschritterstellenCreateView(FormView):

#     form_class = SchrittundKomponentenMultiForm

#     template_name = 'Anleitungsschritterstellen.html'


