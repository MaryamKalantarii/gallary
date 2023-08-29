from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path("",home,name="home"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("services",services,name="services"),
    path("gallery",gallery,name="gallery"),
    path("gallery_single",gallery_single,name="gallery_single"),
    
]