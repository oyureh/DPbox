from django.shortcuts import render, redirect
from contact.models import Usuarios 
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password 
from django.contrib import messages, auth


def index(request):
    return render(
        request,
        'contact/index.html'
    )

@login_required
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

def login(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        gmail = request.POST.get('gmail')
        senha = request.POST.get('senha')

        if not all([nome, gmail, senha]):
            return HttpResponse("Todos os campos são obrigatórios!", status=400)

        try:
            # Criação do usuário usando o manager
            novo_usuario = Usuarios.objects.create_user(
                email=gmail,
                password=senha,
                nome=nome,
            )
        except IntegrityError:
            return HttpResponse("Este e-mail já está cadastrado!", status=400)
        
        return redirect('index')
    
    return render( request, 'contact/login.html')

def login_telasMaiores(request):  
    if request.method == 'POST':     
        email = request.POST.get('gmail')
        senha = request.POST.get('senha')
        print(f"E-mail recebido: {email}, Senha recebida: {senha}") 

        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('index')
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
            return redirect('login')

    return render(request, 'contact/login.html')

def usuarios (request):
    # Tratamento para requisições GET
    usuarios = Usuarios.objects.all()
    paginator = Paginator(usuarios, 5)  
    #paginação
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "contact/usuarios.html", {"page_obj": page_obj})

def login_mobile(request):
    if request.method == 'POST':
        gmail = request.POST['gmail'] 
        senha = request.POST['senha']
        user = authenticate(request, username=gmail, password=senha)
        if user is not None:
            login(request, user)
            messages.error(request, 'Login realizado com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'E-mail ou senha inválidos.')

    return render(request, 'cadastro.html')
