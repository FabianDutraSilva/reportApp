# Generated by Django 4.1.7 on 2023-04-06 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_reporte_rrhh_reporte_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='titulo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
