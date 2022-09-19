from django.shortcuts import render, redirect
from django.views import generic
from .models import Equipo, Estadio, Jugador
from .forms import EquipoForm, EstadioForm, JugadorForm

# Create your views here.

def index(request):
    return render(request, "index.html")

#C R U D 
#---------------------------------------------------------Equipos
class DeleteEquipo(generic.View):
    template_name = "app1/deleteEquipo.html"
    context = {}

    def get(self, request, pk, *args, **kwargs):
        queryset = Equipo.objects.get(pk=pk)
        self.context = {
            "equipo": queryset
        }
        return render(request, self.template_name, self.context)

    def post(self, request, pk, *args, **kwargs):
        if request.method=='POST':
            equipos = Equipo.objects.get(pk=pk)
            equipos.delete()
            return redirect("app1:equipos_view")

def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "app1/equipos.html", {"equipos": equipos})


class CreateEquipo(generic.View):
    template_name = "app1/createEquipo.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = EquipoForm()
        if request.user.is_authenticated:
            error = "Se encuentra en sesión"
        else: 
            error = "Por favor inicie sesión"
        self.context = {
            "form": form,
            "message": error
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = EquipoForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("app1:equipos_view")

def update(request):
    context = {
    }
    return render (request, "app1/update.html", context)

class EditarEquipo(generic.View):
    template_name = "app1/editarEquipo.html"
    context = {}

    def get(self, request, pk, *args, **kwargs):
        queryset = Equipo.objects.get(pk=pk)
        form = EquipoForm(instance=queryset)
        self.context = {
            "form": form
        }
        return render(request, self.template_name, self.context)

    def post(self, request, pk, *args, **kwargs):
        if request.method=='POST':
            form = EquipoForm(request.POST)
            if form.is_valid():
                equipo = Equipo.objects.get(pk=pk)
                equipo.Nombre = form.cleaned_data.get('Nombre')
                equipo.Entrenador = form.cleaned_data.get('Entrenador')
                equipo.Num_jugadores = form.cleaned_data.get('Num_jugadores')
                equipo.Num_partidos = form.cleaned_data.get('Num_partidos')
                equipo.Puntos_temp = form.cleaned_data.get('Puntos_temp')
                equipo.Clasificacion = form.cleaned_data.get('Clasificacion')
                equipo.save()
                return redirect("app1:equipos_view")

#---------------------------------------------------------Estadios
class DeleteEstadio(generic.View):
    template_name = "app1/deleteEstadio.html"
    context = {}

    def get(self, request, pk, *args, **kwargs):
        queryset = Estadio.objects.get(pk=pk)
        self.context = {
            "estadio": queryset
        }
        return render(request, self.template_name, self.context)

    def post(self, request, pk, *args, **kwargs):
        if request.method=='POST':
            estadios = Estadio.objects.get(pk=pk)
            estadios.delete()
            return redirect("app1:estadios_view")

def estadios(request):
    estadios = Estadio.objects.all()
    return render(request, "app1/estadios.html", {"estadios": estadios})


class CreateEstadio(generic.View):
    template_name = "app1/createEstadio.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = EstadioForm()
        if request.user.is_authenticated:
            error = "Se encuentra en sesión"
        else: 
            error = "Por favor inicie sesión"
        self.context = {
            "form": form,
            "message": error
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = EstadioForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("app1:estadios_view")

def update(request):
    context = {
    }
    return render (request, "app1/update.html", context)

class EditarEstadio(generic.View):
    template_name = "app1/editarEstadio.html"
    context = {}

    def get(self, request, pk, *args, **kwargs):
        queryset = Estadio.objects.get(pk=pk)
        form = EstadioForm(instance=queryset)
        self.context = {
            "form": form
        }
        return render(request, self.template_name, self.context)


    def post(self, request, pk, *args, **kwargs):
        if request.method=='POST':
            form = EstadioForm(request.POST)
            if form.is_valid():
                estadio = Estadio.objects.get(pk=pk)
                estadio.Nombre = form.cleaned_data.get('Nombre')
                estadio.Dueño = form.cleaned_data.get('Dueño')
                estadio.Capacidad = form.cleaned_data.get('Capacidad')
                estadio.Eqs_partido = form.cleaned_data.get('Eqs_partido')
                estadio.save()
                return redirect("app1:estadios_view")

#---------------------------------------------------------Jugadores
class DeleteJugador(generic.View):
    template_name = "app1/deleteJugador.html"
    context = {}

    def get(self, request, pk, *args, **kwargs):
        queryset = Jugador.objects.get(pk=pk)
        self.context = {
            "jugador": queryset
        }
        return render(request, self.template_name, self.context)

    def post(self, request, pk, *args, **kwargs):
        if request.method=='POST':
            jugadores = Jugador.objects.get(pk=pk)
            jugadores.delete()
            return redirect("app1:jugadores_view")

def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, "app1/jugadores.html", {"jugadores": jugadores})


class CreateJugador(generic.View):
    template_name = "app1/createJugador.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = JugadorForm()
        if request.user.is_authenticated:
            error = "Se encuentra en sesión"
        else: 
            error = "Por favor inicie sesión"
        self.context = {
            "form": form,
            "message": error
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = JugadorForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("app1:jugadores_view")

def update(request):
    context = {
    }
    return render (request, "app1/update.html", context)

class EditarJugador(generic.View):
    template_name = "app1/editarJugador.html"
    context = {}

    def get(self, request, pk, *args, **kwargs):
        queryset = Jugador.objects.get(pk=pk)
        form = JugadorForm(instance=queryset)
        self.context = {
            "form": form
        }
        return render(request, self.template_name, self.context)


    def post(self, request, pk, *args, **kwargs):
        if request.method=='POST':
            form = JugadorForm(request.POST)
            if form.is_valid():
                jugador = Jugador.objects.get(pk=pk)
                jugador.Nombre = form.cleaned_data.get('Nombre')
                jugador.Edad = form.cleaned_data.get('Edad')
                jugador.Numero = form.cleaned_data.get('Numero')
                jugador.Eq_actual = form.cleaned_data.get('Eq_actual')
                jugador.Fecha_ingreso = form.cleaned_data.get('Fecha_ingreso')
                jugador.save()
                return redirect("app1:jugadores_view")