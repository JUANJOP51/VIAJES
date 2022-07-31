from urllib import request
from django.shortcuts import render
from Articulos.models import Region
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def home(request):
    articulos = Region.objects.all()
    return render(request, 'bienvenida.html', {'articulos': articulos})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form. is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            usuario = authenticate(username=usuario, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, 'Articulos/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render(request, 'Articulos/login.html', {'mensaje': 'Usuario o clave incorrecta'})

        else:
            return render(request, 'Articulos/login.html', {'mensaje': f'FORMULARIO INVALIDO'})

    else:
        form = AuthenticationForm()
        render (request, 'Articulos/login.html', {'form': form})
            



# Create your views here.
