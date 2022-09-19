# Generated by Django 4.1.1 on 2022-09-18 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=70)),
                ('Entrenador', models.CharField(max_length=50)),
                ('Num_jugadores', models.IntegerField()),
                ('Num_partidos', models.IntegerField()),
                ('Puntos_temp', models.IntegerField()),
                ('Clasificacion', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=70)),
                ('Dueño', models.CharField(max_length=70)),
                ('Capacidad', models.IntegerField()),
                ('Eqs_partido', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=70)),
                ('Edad', models.IntegerField()),
                ('Numero', models.IntegerField()),
                ('Eq_actual', models.CharField(max_length=70)),
                ('Fecha_ingreso', models.DateField()),
            ],
        ),
    ]