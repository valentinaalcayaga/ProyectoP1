# Generated by Django 3.2.3 on 2021-07-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='id',
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='fecha',
            field=models.DateTimeField(primary_key=True, serialize=False, verbose_name='Fecha'),
        ),
    ]