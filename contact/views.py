from django.shortcuts import render, redirect #get_object_or_404
from contact.models import Usuarios 
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password 


def index(request):
    return render(
        request,
        'contact/index.html'
    )

def login(request):
    return render( request, 'contact/login.html')

def quemsomos(request):
    return render(
        request,
        'contact/quemsomos.html'
    )

def _header_usuarios(request):
    return render(
        request,
        'contact/_header_usuarios'
    )

def cadastro(request):
    return render(
        request,
        'contact/cadastro.html'
    )

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        gmail = request.POST.get('gmail')
        senha = request.POST.get('senha')

        if not all([nome, gmail, senha]):
            return HttpResponse("Todos os campos são obrigatórios!", status=400)

        senha_hash = make_password(senha)

        try:
            novo_usuario = Usuarios(
                nome=nome,
                gmail=gmail,
                senha=senha_hash  # Salva a senha criptografada
            )
            
            novo_usuario.save()
        except IntegrityError:
            return HttpResponse("Este e-mail já está cadastrado!", status=400)

        return redirect('index')

    # Tratamento para requisições GET
    usuarios = Usuarios.objects.all()
    paginator = Paginator(usuarios, 5)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "contact/usuarios.html", {"page_obj": page_obj})

