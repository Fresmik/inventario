# Generated by Django 4.1.6 on 2023-02-22 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_productos_pvp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='pvp',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=9),
        ),
    ]
