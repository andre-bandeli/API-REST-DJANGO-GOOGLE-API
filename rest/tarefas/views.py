from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Tarefa
from .forms import TarefaForms



@login_required
def listar_tarefas(request):
    data = {}
    data['db'] = Tarefa.objects.all()
    return render(request,  'list.html', data )

def form_list(request):
    if request.method == "GET":
         return render(
            request, "form.html",
            {"form_list": TarefaForms}
        )
    elif request.method == "POST":
        form = TarefaForms(request.POST)
        if form_list.is_valid():
            user = form_list.save()
            return render(request, 'home.html')