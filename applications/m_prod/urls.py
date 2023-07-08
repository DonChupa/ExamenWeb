from django.urls import path
from .views import mostrar_producto, carro, boleta,borrar_boleta, borrar_carro, borrar_todo_carro, crear_inventario, crear_producto, eliminar_producto, editar_producto, listar_producto
urlpatterns = [
    path('todos/', mostrar_producto,  name = 'productos'),
    path('crear-inventario/<int:producto_id>/', crear_inventario, name = 'crear_inventario'),
    path('carrito/',carro,name = 'carrito'),
    path('borrar/<int:producto_id>/', borrar_carro,name = 'borrar'),
    path('borrar-todo/', borrar_todo_carro,name = 'borrartodo'),


    path('crear_producto/', crear_producto, name='crear_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('listar_producto/', listar_producto, name='listar_producto' ),
    path('boleta/', boleta, name = 'boleta'),
    path('borrar-boleta/',borrar_boleta, name='borrar_boleta')
]