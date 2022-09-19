from django.db import models

# Create your models here.
class Equipo(models.Model):
    Nombre = models.CharField(max_length=70)
    Entrenador = models.CharField(max_length=50)
    Num_jugadores = models.IntegerField()
    Num_partidos = models.IntegerField()
    Puntos_temp = models.IntegerField()
    Clasificacion = models.BooleanField(default=False)

    def __str__(self):
        return self.Nombre

class Estadio(models.Model):
    Nombre = models.CharField(max_length=70)
    Dueño = models.CharField(max_length=70)
    Capacidad = models.IntegerField()
    Eqs_partido = models.CharField(max_length=120)

    def __str__(self):
        return self.Nombre

class Jugador(models.Model):
    Nombre = models.CharField(max_length=70)
    Edad = models.IntegerField()
    Numero = models.IntegerField()
    Eq_actual = models.CharField(max_length=70)
    Fecha_ingreso = models.DateField()

    def __str__(self):
        return self.Nombre

