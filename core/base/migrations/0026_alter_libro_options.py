# Generated by Django 4.1.6 on 2023-03-04 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_libro_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
    ]
