from django.shortcuts import render, redirect
from contact.models import Usuarios 


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

# def usuarios(request):
#     return render(
#         request,
#         'contact/usuarios.html'
#     )

# def usuarios(request):
#     contacts = Usuarios.objects.all()

#     context ={
#         'contacts': contacts,
#     }

#     return render(
#         request,
#         'contact/usuarios.html',
#         context
#     )

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuarios(
            nome=request.POST.get('nome'),
            gmail=request.POST.get('gmail'), 
            senha=request.POST.get('senha')  
        )

        novo_usuario.save()
        return redirect('index')  

    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    return render(request, 'contact/usuarios.html', usuarios)

