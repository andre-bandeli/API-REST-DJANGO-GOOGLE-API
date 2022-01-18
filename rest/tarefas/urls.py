
from django.urls import path

from .views import listar_tarefas


urlpatterns = [
    path('list', listar_tarefas, name="list"),
]
