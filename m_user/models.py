from django.db.models import Model, IntegerField, ForeignKey, CASCADE
from django.contrib.auth.models import User
from m_prod.models import Boleta
# Create your models here.

class DetalleBoleta(Model):
    id = IntegerField(default= 1, primary_key= True)
    boleta = ForeignKey(Boleta, on_delete= CASCADE, primary_key= True)