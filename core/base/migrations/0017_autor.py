# Generated by Django 4.1.7 on 2023-03-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rename_productos_detallesuministro_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['nombres'],
            },
        ),
    ]
