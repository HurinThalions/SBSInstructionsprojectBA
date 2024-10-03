from datetime import timedelta
from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from betterforms.multiform import MultiModelForm

from .models import Profil, Anleitung, Anleitungsschritt, Komponente

# Formular zum Erstellen ein Accounts
# Nur valide e-mail adreesen werden akzeptiert und individuelle benutzernamen
class SignupForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, help_text='Required. Enter a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Profil
        fields = ('benutzername', 'email', 'password')


# Formular zu einloggen
# Benutzername kann auch verwendet werden
class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)

    class Meta:
        fields = ('email', 'password')


# Formular um Anleitungen zu erstellen
class AnleitungForm(forms.ModelForm):

    # Dauer wird in Minute aufgenommen
    dauer = forms.IntegerField(label='Dauer (in Minuten)')

    class Meta:
        model = Anleitung
        fields = ('profil', 'anleittitel', 'kategorie', 'dauer', 'datum', 'img')

    # Einstellung das Dauer in Minuten aufgenommen werden kann
    def clean_dauer(self):
        dauer = self.cleaned_data['dauer']
        dauer_in_minuten = timedelta(minutes=dauer)
        return dauer_in_minuten
    

# Formular um Anleitungsschritte zu erstellen
class AnleitungsschrittForm(forms.ModelForm):
    class Meta:
        model = Anleitungsschritt
        fields = ('anleitung', 'schrittbenennung', 'beschreibung', 'schrittbild')
        exclude = ('anleitung',)

    def save_with_anleitung_id(self, anleitung):
        form = super().save(commit=False)
        form.anleitung = anleitung
        form.save()
        return form

class KomponenteForm(forms.ModelForm):
    class Meta:
        model = Komponente
        fields = ['anleitungsschritt', 'kompbeschreibung', 'kompbild']
        exclude = ('anleitungsschritt',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['kompbeschreibung'].required = False
    #     self.fields['kompbild'].required = False


    def save_with_anleitungsschritt_id(self, anleitungsschritt):
        form = super().save(commit=False)
        form.anleitungsschritt = anleitungsschritt
        form.save()
        return form

# Formular um Anleitungsschritte und Komponenten in einem Schritt zu erfassen
# Gleichzeitige Abspeicherung noch nicht möglich
# class SchrittundKomponentenMultiForm(MultiModelForm):
#     form_classes = {
#         'Anleitungsschritt': AnleitungsschrittForm,
#         'Komponente': KomponenteForm,
#     }

