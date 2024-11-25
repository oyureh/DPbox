from django.shortcuts import render


def index(request):
    return render(
        request,
        'contact/index.html'
    )

def login(request):
    return render(
        request,
        'contact/login.html'
    )

def quemsomos(request):
    return render(
        request,
        'contact/quemsomos.html'
    )

def usuarios(request):
    return render(
        request,
        'contact/usuarios.html'
    )

from contact.models import Usuarios 

def usuarios(request):
    contacts = usuarios.objects.all()
    # no django esta dizendo que o erro esta no objects
    context ={
        'contacts': contacts,
    }

    return render(
        request,
        'contact/usuarios.html',
        context
    )
