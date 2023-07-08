from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE,TextField, DecimalField, ImageField, AutoField
from django.contrib.auth.models import User

# Create your models here.

class Producto(Model):
    id = AutoField(primary_key= True)
    nombre_artista = CharField(max_length=100, null = False)
    nombre_album = CharField(max_length=100, null = False)
    año = IntegerField(null = False)
    precio = DecimalField(max_digits=8, decimal_places=2)
    img = ImageField(upload_to="prod", blank=True)
    tipo = CharField(null= False, max_length=100)


class Boleta(Model):
    id_usuario = ForeignKey(User,on_delete = CASCADE)
    id_producto = ForeignKey(Producto, on_delete = CASCADE)
    cantidad = IntegerField(null = False)