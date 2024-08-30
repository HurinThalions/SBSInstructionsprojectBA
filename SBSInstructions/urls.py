from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from . import views

urlpatterns = [

    # Url fuer Klassenbasierter StartseitenView
    path('', views.StartseiteListView.as_view(), name='katalog_detail_view'),

    # Anleitung, Anleitungsschritte und Komponenten werden erstellt
    path('anleitungerstellen', views.AnleitungerstellenCreateView.as_view(), name='anleitungerstellen_add_page_create_view'),
    path('anleitungsschritteerstellen', views.AnleitungsschritterstellenCreateView.as_view(), name='anleitungsschritteerstellen_add_page_create_view'),
    path('komponentenerstellen', views.KomponentenerstellenCreateView.as_view(), name='komponentenerstellen_createview'),

    # Anleitung koennen hier durchgeklickt werden
    path('anleitungdurchgehen/<int:pk>', views.AnleitungdurchgehenDetailView.as_view(), name='anleitungdurchgehen_detail_view'),
    
    # Profil wird erstellt, Nutzer wird eingeloggt und Private Nutzerseite
    path('profilerstellen', views.ProfilerstellenCreateView.as_view(), name='profilerstellen_create_view'),
    path('login', views.ProfileinloggenLoginView.as_view(), name='Profileinloggen_login_view'),
    path('profileigeneanleitungen/<int:pk>', views.ProfileigeneAnleitungenDetailView.as_view(), name='profileigeneanleitungen'),

    # Endseiten nach Erstellung und durchklicken von Anleitungen
    # sind rein statisch
    path('anleitungfertig', views.anleitungfertig, name='anleitungfertig'),
    path('entwurffertig', views.entwurffertig, name='entwurffertig'),
    path('anleitunggespeichert', views.anleitunggespeichert, name='anleitunggespeichert'),
    
]
urlpatterns += staticfiles_urlpatterns()

