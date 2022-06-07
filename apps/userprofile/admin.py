from django.contrib import admin

# Register your models here.
from .models import Profile #Questa riga importa il modello definito in models

admin.site.register(Profile) #Questa riga rende visibile il modello nella console di admin di Django