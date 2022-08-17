from django.urls import path
from . import views

urlpatterns = [
    path('master' ,views.google_master,name='master'), 
    path('home' ,views.google_home,name='home'),
    path('about' ,views.google_about,name='about'),
    path('contact' ,views.google_contact,name='contact'),

]