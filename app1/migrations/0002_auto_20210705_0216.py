# Generated by Django 3.2.3 on 2021-07-05 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='rut',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Ingrese rut sin -'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='rut',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Ingrese rut sin -'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='rut',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Ingrese rut sin -'),
        ),
    ]