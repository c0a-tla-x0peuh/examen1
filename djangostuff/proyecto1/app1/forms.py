from django import forms

from .models import Equipo, Estadio, Jugador

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            "Nombre",
            "Entrenador",
            "Num_jugadores",
            "Num_partidos",
            "Puntos_temp",
            "Clasificacion"
        ]

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = [
            "Nombre",
            "Dueño",
            "Capacidad",
            "Eqs_partido"
        ]

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
            "Nombre",
            "Edad",
            "Numero",
            "Eq_actual",
            "Fecha_ingreso"
        ]