# Generated by Django 4.2 on 2024-08-12 03:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=150)),
                ('cedula', models.BigIntegerField()),
                ('telefono', models.BigIntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('marca', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('procesador', models.CharField(max_length=100)),
                ('pantalla', models.TextField(max_length=200)),
                ('ram', models.IntegerField()),
                ('camara', models.TextField(max_length=300)),
                ('almacenamiento', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='celulares_images')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalogo_celular.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
                ('fecha_compra', models.DateField()),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalogo_celular.cliente')),
                ('productos', models.ManyToManyField(to='catalogo_celular.producto')),
            ],
        ),
    ]
