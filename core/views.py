from django.http import response
from django.shortcuts import redirect, render
from core.models import Evento

# Create your views here.


def index(request):  # redirecionar para /agenda como default
    return redirect("/agenda/")


def list_eventos(request):
    evento = Evento.objects.all()
    dados = {"eventos": evento}
    return render(request, "agenda.html", dados)
