# Generated by Django 4.1.6 on 2023-02-16 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_categoria_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]
