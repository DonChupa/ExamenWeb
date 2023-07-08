from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from .forms import FormularioEntrar, NuevoRegistro
from sweetify import info, success, warning
# from sweetify import info, success, warning, error
# Create your views here.

def mostrar_entrar(request):
    print('hola')
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'formulario':FormularioEntrar(),
        }
        return render(request,'iniciar_sesion.html',contexto)
    if request.method == 'POST':
        datos_usuario = FormularioEntrar(data = request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            print('hola')
            usuario = authenticate(
                username = datos_usuario.cleaned_data['usuario'],
                password = datos_usuario.cleaned_data['contrasenia_usuario']
            )
            if usuario is not None:
                print('hola')
                login(request, usuario)
                success(request, f'Bienvenido {usuario.username}')
                return redirect('index')
        warning(request, 'Usuario y contraseña invalidos :(')
        contexto = {
            'formulario': datos_usuario
        }
        return render(request,'iniciar_sesion.html', contexto)

def mostrar_registro(request):
    print(request.method)
    if request.method == 'GET':
        print('GET')
        contexto = {
            'formulario': NuevoRegistro()
        }
        return render(request, 'registrar.html', contexto)
    if request.method == 'POST':
        print('POST')
        formulario_registro = NuevoRegistro(data=request.POST)
        es_valido = formulario_registro.is_valid() 
        if es_valido: 
            usuario_nuevo = formulario_registro.save()
            success(request,'Gracias por unirte :)')
            return redirect('index')
        contexto = {
            'formulario': formulario_registro
        }
        warning(request,' Ups... observe los campos con errres y reintente')
        return render(request,'registrar.html',contexto)

def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(request, 'Sesión cerrada :D')
    return redirect('index')