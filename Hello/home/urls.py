from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'), 
    path("services",views.services,name='services'), 
    path("contact",views.contact,name='contact'),
    path("update_item/",views.updateItem,name='update_item')
    
    # path("Icecream",views.Icecream,name='Icecream')
    ]  