from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import (
    Form,
    CharField,
    PasswordInput,
    EmailField,
    EmailInput,
    CheckboxInput,
    BooleanField,
    TextInput
)


class NuevoRegistro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = { 'class':'form-control' }
        self.fields['password2'].widget.attrs = { 'class':'form-control' }
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email'
        ]
        widgets = {
            'username': TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'email': EmailInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }

class FormularioEntrar(Form):
    usuario = CharField(
        required = True,
        label = 'Ingrese su usuario',
        widget = TextInput(
            attrs = {
                'class':'form-control',
            }
        )
    )
    contrasenia_usuario = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        label = 'Ingrese su contraseña',
        widget = PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    recuerdame = BooleanField(
        required = False,
        label = 'Recordarme',
        widget = CheckboxInput(

        )
    )
