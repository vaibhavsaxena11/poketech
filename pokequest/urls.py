from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^event$', views.event, name='event'),
    url(r'^event_submit$', views.event_submit, name='event_submit'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^instructions$', views.instructions, name='instructions'),
    url(r'^pokedex$', views.pokedex, name='pokedex'),
    url(r'^scorepage$', views.scorepage, name='scorepage'),
]