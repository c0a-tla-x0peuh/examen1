from django.urls import path

from . import views

app_name = "app1"

urlpatterns = [
    path('', views.index, name="index_view"),
    path('equipos/', views.equipos, name="equipos_view"),
    path('equipos/crear/', views.CreateEquipo.as_view(), name="createEquipo_view"),
    path('equipos/editar/<int:pk>/', views.EditarEquipo.as_view(), name="editarEquipo_view"),
    path('equipos/eliminar/<int:pk>/', views.DeleteEquipo.as_view(), name="deleteEquipo_view"),

    path('estadios/', views.estadios, name="estadios_view"),
    path('estadios/crear/', views.CreateEstadio.as_view(), name="createEstadio_view"),
    path('estadios/editar/<int:pk>/', views.EditarEstadio.as_view(), name="editarEstadio_view"),
    path('estadios/eliminar/<int:pk>/', views.DeleteEstadio.as_view(), name="deleteEstadio_view"),

    path('jugadores/', views.jugadores, name="jugadores_view"),
    path('jugadores/crear/', views.CreateJugador.as_view(), name="createJugador_view"),
    path('jugadores/editar/<int:pk>/', views.EditarJugador.as_view(), name="editarJugador_view"),
    path('jugadores/eliminar/<int:pk>/', views.DeleteJugador.as_view(), name="deleteJugador_view")
]
