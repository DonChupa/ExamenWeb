from django.shortcuts import render, redirect
from .models import Producto, Boleta
from .forms import FormularioProducto
from sweetify import success, warning
from django.contrib.auth.models import User

# Create your views here.
def mostrar_producto(request):
    lista = []
    prod = Producto.objects.all()
    for p in prod:
            i = {
                'nombre_artista': p.nombre_artista,
                'img': p.img,
                'nombre_album': p.nombre_album,
                'precio': p.precio,
                'año': p.año,
                'tipo': p.tipo,
                'id': p.id
            }
            lista.append(i)
    con = {
            'productos': lista
        }
    return render(request, 'producto/productos.html', con)


def carro(request):
    lista = []
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            user = None
        if user is None:
            return render(request, 'producto/carrito.html')
        
        try:
            existe = Boleta.objects.filter(id_usuario=request.user.id)
        except Boleta.DoesNotExist:
            existe = None
        
        if existe is None:
            return render(request, 'producto/carrito.html')
        else:
            for i in existe:
                prod = Producto.objects.get(id = i.id_producto.id)
                dic = {
                    'producto': prod.nombre_album,
                    'cantidad': i.cantidad,
                    'tipo': prod.tipo,
                    'precio': prod.precio * i.cantidad,
                    'id': prod.id
                }
                lista.append(dic)
            
            cont = {
                'producto': lista
            }
            
            return render(request, 'producto/carrito.html', cont)
    else:
        return render(request, 'producto/carrito.html')


def borrar_carro(request, producto_id):
    prod = Producto.objects.get(id = producto_id)
    Boleta.objects.filter(id_producto = prod).first().delete()
    success(request,'borrado :D')
    return redirect('carrito')



def boleta(request):
    total = 0
    productos = Boleta.objects.filter(id_usuario= request.user)
    lista = []
    nombre = request.user.username
    for i in productos:
        producto = Producto.objects.get(id = i.id_producto.id)
        total += producto.precio
        lista.append( {'nombre':producto.nombre_album, 'precio': producto.precio})
    cont = {
        'total': total,
        'lista': lista,
        'nombre': nombre
    }
    return render(request,'producto/boleta.html', cont)


def borrar_boleta(request):
    Boleta.objects.filter(id_usuario = request.user).delete()
    success(request, 'gracias por comprar con nosotros')
    return redirect('index')

def borrar_todo_carro(request):
    Boleta.objects.filter(id_usuario = request.user).delete()
    success(request, 'carrito limpiado')
    return redirect('carrito')

def crear_inventario(request , producto_id):
    if not request.user.is_authenticated:
        warning(request, 'necesita iniciar sesion para comprar')
        return redirect('mostrar_entrar')
    inventario =  Boleta.objects.create(
    id_usuario = request.user,
    id_producto = Producto.objects.get(id = producto_id),
    cantidad = 1
            )
    success(request,'producto agregado :D')
    inventario.save()
    return redirect('productos')


def crear_producto(request):
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Producto añadido correctamente')
            return redirect('listar_producto')
    else:
        context = {'form': FormularioProducto()}
    return render(request, 'producto/crear_producto.html', context)

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    success(request, 'Producto eliminado correctamente')
    return redirect('listar_producto')

def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        formulario = FormularioProducto(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Producto actualizado correctamente')
            return redirect('listar_producto')
    else:
        formulario = FormularioProducto(instance=producto)

    context = {'form': formulario}
    return render(request, 'producto/editar_producto.html', context)

def listar_producto(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'producto/listar_producto.html', context)

