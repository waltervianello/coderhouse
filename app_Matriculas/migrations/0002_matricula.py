# Generated by Django 3.0.1 on 2022-10-13 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_Matriculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('tipo', models.CharField(choices=[('ORDINARIA', 'ORDINARIA'), ('EXTRAORDINARIA', 'EXTRAORDINARIA'), ('ESPECIAL', 'ESPECIAL')], default='disponible', max_length=45)),
                ('fecha', models.DateField()),
                ('curso', models.CharField(choices=[('1', 'I CICLO'), ('2', 'II CICLO'), ('3', 'III CICLO'), ('4', 'IV CICLO'), ('5', 'V CICLO')], default='disponible', max_length=45)),
                ('carrera', models.CharField(max_length=100)),
                ('fk_alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_Matriculas.Alumno')),
            ],
        ),
    ]
