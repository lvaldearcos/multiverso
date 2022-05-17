from django.urls import path

from marvel.views import *

urlpatterns = [
    path('', index),
    path('crear_pagina', crear),
    path('crear', crear_personaje),
    path('actualizar/<int:id>', editar_personaje),
    path('eliminar/<int:id>', borrar_personaje),
]