
from django.urls import path

from .views import delete, listar_tarefas, editar


urlpatterns = [
    path('list', listar_tarefas, name="list"),
    path('delete/<int:pk>/', delete, name='delete'),
    path('editar/<int:pk>/', editar, name='edit'),
]
