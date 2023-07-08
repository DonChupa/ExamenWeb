from django.shortcuts import render

from django.shortcuts import render, redirect
from applications.registrar.forms import FormularioEntrar, NuevoRegistro
from sweetify import success, warning
from django.contrib.auth.models import User

# Create your views here.

def crear_usuario(request):
    if request.method == 'POST':
        formulario = NuevoRegistro(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Usuario añadido correctamente')
            return redirect('listar_usuario')
        context = {'form': formulario}
        warning(request, 'datos incorrectos')
    return render(request, 'usuario/crear_usuario.html', context)

def eliminar_usuario(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    success(request, 'Usuario eliminado correctamente')
    return redirect('listar_usuario')

def editar_usuario(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        formulario = NuevoRegistro(request.POST, instance=user)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Usuario actualizado correctamente')
            return redirect('listar_usuario')
    else:
        formulario = NuevoRegistro(instance=user)

    context = {'form': formulario}
    return render(request, 'usuario/editar_usuario.html', context)

def listar_usuario(request):
    user = User.objects.all()
    context = {
        'usuarios': user
    }
    return render(request, 'usuario/listar_usuario.html', context)


