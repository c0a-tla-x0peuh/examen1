from django.contrib import admin
from .models import Equipo, Estadio, Jugador

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Estadio)
admin.site.register(Jugador)