# Generated by Django 4.1.7 on 2023-03-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_ubicaciones_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('serie', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('centroCosto', models.CharField(max_length=200)),
                ('prioridad', models.CharField(max_length=200)),
                ('parteDe', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='ubicacion',
            old_name='centroDeCosto',
            new_name='centroCosto',
        ),
        migrations.RenameField(
            model_name='ubicacion',
            old_name='codigoDelActivo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='ubicacion',
            old_name='esParteDe',
            new_name='parteDe',
        ),
        migrations.RenameField(
            model_name='ubicacion',
            old_name='tipoDeLocalizacion',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='ubicacion',
            name='text',
        ),
    ]
