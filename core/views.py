from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):  # redirecionar para /agenda como default
    return redirect("/agenda/")


def login_user(request):
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/")


def submit_log(request):
    if request.POST:
        username = request.POST.get(
            "username"
        )  # Pega o valor do input username da request
        password = request.POST.get(
            "password"
        )  # Pega o valor do input password da request

        usuario = authenticate(
            username=username, password=password
        )  # Faz a verificação do usuario

        if usuario is not None:
            login(request, usuario)
            return redirect("/")
        else:
            messages.error(request, "Usuario ou senha inválidos")
    return redirect("/")


@login_required(login_url="/login/")
def list_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario=user)
    dados = {"eventos": evento}
    return render(request, "agenda.html", dados)
