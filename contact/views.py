from django.shortcuts import render, redirect
from contact.models import Usuarios 
from django.http import HttpResponse
from django.db import IntegrityError


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

def usuarios(request):
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        gmail = request.POST.get('gmail')
        senha = request.POST.get('senha')

        if not all([nome, gmail, senha]):
            return HttpResponse("Todos os campos são obrigatórios!", status=400)

        try:
            novo_usuario = Usuarios(
                nome=nome,
                gmail=gmail,
                senha=senha
            )
            novo_usuario.save()
        except IntegrityError:
            return HttpResponse("Este e-mail já está cadastrado!", status=400)

        return redirect('index')  
        
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    return render(request, 'contact/usuarios.html', usuarios)