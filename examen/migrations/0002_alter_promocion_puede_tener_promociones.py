# Generated by Django 5.1.4 on 2024-12-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocion',
            name='puede_tener_promociones',
            field=models.BooleanField(null=True),
        ),
    ]