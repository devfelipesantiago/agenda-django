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


@login_required(login_url="/login/")  # Requer autenticação do login
def list_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario=user)
    dados = {"eventos": evento}
    return render(request, "agenda.html", dados)


@login_required(login_url="/login/")
def evento(request):
    id_evento = request.GET.get("id")
    print(id_evento)
    dados = {}
    if id_evento:
        dados["evento"] = Evento.objects.get(id=id_evento)
    return render(request, "evento.html", dados)


# Pegar os dados do submit
@login_required(login_url="/login/")
def submit_evento(request):
    if request.POST:
        title = request.POST.get("title")
        data_evento = request.POST.get("data_evento")
        descricao = request.POST.get("descricao")
        usuario = request.user
        # Atualizar os dados
        id_evento = request.POST.get("id_evento")
        if id_evento:
            Evento.objects.filter(id=id_evento).update(
                title=title,
                data_evento=data_evento,
                description=descricao,
            )
        else:
            # Agora temos que registrar os dados coletados
            Evento.objects.create(
                title=title,
                data_evento=data_evento,
                description=descricao,
                usuario=usuario,
            )  # Os campos iguais das colunas da tabela
    return redirect("/")


@login_required(login_url="/login/")
def delete_evento(request, id_evento):
    ususario = request.user
    Evento.objects.get(id=id_evento)
    if ususario == evento.usuario:
        evento.delete()
    return redirect("/")
