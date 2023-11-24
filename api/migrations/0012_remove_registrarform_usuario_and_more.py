# Generated by Django 4.2.5 on 2023-10-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_registrarform_apellidos_us_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrarform',
            name='usuario',
        ),
        migrations.AddField(
            model_name='registrarform',
            name='apellidos_us',
            field=models.CharField(db_column='apellidos_us', default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrarform',
            name='nombre_us',
            field=models.CharField(db_column='nombre_us', default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registrarform',
            name='contraseña',
            field=models.CharField(db_column='contraseña_us', max_length=100),
        ),
        migrations.AlterField(
            model_name='registrarform',
            name='correo_us',
            field=models.CharField(db_column='correo_us', max_length=100),
        ),
    ]
