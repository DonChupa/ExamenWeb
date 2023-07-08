from django.urls import path
from .views import crear_usuario, eliminar_usuario, editar_usuario,listar_usuario
urlpatterns = [
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('eliminar_usuario/<int:user_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('editar_usuario/<int:user_id>/', editar_usuario, name='editar_usuario'),
    path('listar_usuario/', listar_usuario, name='listar_usuario' )
    ]