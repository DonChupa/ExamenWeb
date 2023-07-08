# Generated by Django 4.2 on 2023-07-08 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('nombre_artista', models.CharField(max_length=100)),
                ('nombre_album', models.CharField(max_length=100)),
                ('año', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('img', models.ImageField(blank=True, upload_to='prod')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_carrito', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m_prod.producto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
