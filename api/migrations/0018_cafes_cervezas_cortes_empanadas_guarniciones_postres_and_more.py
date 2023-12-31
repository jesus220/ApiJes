# Generated by Django 4.2.5 on 2023-10-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_cafe_cerveza_corte_empanada_guarnicion_postre_precio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafes',
            fields=[
                ('Id_cafes', models.AutoField(primary_key=True, serialize=False)),
                ('cafes', models.CharField(db_column='Cafes', max_length=100)),
            ],
            options={
                'db_table': 'Cafes',
            },
        ),
        migrations.CreateModel(
            name='Cervezas',
            fields=[
                ('Id_cervezas', models.AutoField(primary_key=True, serialize=False)),
                ('cervezas', models.CharField(db_column='Cervezas', max_length=100)),
            ],
            options={
                'db_table': 'Cervezas',
            },
        ),
        migrations.CreateModel(
            name='Cortes',
            fields=[
                ('Id_cortes', models.AutoField(primary_key=True, serialize=False)),
                ('cortes', models.CharField(db_column='Cortes', max_length=100)),
            ],
            options={
                'db_table': 'Cortes',
            },
        ),
        migrations.CreateModel(
            name='Empanadas',
            fields=[
                ('Id_empanadas', models.AutoField(primary_key=True, serialize=False)),
                ('empanadas', models.CharField(db_column='Empanadas', max_length=100)),
            ],
            options={
                'db_table': 'Empanadas',
            },
        ),
        migrations.CreateModel(
            name='Guarniciones',
            fields=[
                ('Id_guarniciones', models.AutoField(primary_key=True, serialize=False)),
                ('guarniciones', models.CharField(db_column='Guarniciones', max_length=100)),
            ],
            options={
                'db_table': 'Guarniciones',
            },
        ),
        migrations.CreateModel(
            name='Postres',
            fields=[
                ('Id_postres', models.AutoField(primary_key=True, serialize=False)),
                ('postres', models.CharField(db_column='Postres', max_length=100)),
            ],
            options={
                'db_table': 'Postres',
            },
        ),
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('Id_precio', models.AutoField(primary_key=True, serialize=False)),
                ('precios', models.CharField(db_column='Precios', max_length=100)),
            ],
            options={
                'db_table': 'Precios',
            },
        ),
        migrations.CreateModel(
            name='Refrescos',
            fields=[
                ('Id_refrescos', models.AutoField(primary_key=True, serialize=False)),
                ('refrescos', models.CharField(db_column='Refrescos', max_length=100)),
            ],
            options={
                'db_table': 'Refrescos',
            },
        ),
        migrations.CreateModel(
            name='SalsaPastas',
            fields=[
                ('Id_salsapastas', models.AutoField(primary_key=True, serialize=False)),
                ('salsapastas', models.CharField(db_column='SalsaPasta', max_length=100)),
            ],
            options={
                'db_table': 'SalsaPasta',
            },
        ),
        migrations.DeleteModel(
            name='Cafe',
        ),
        migrations.DeleteModel(
            name='Cerveza',
        ),
        migrations.DeleteModel(
            name='Corte',
        ),
        migrations.DeleteModel(
            name='Empanada',
        ),
        migrations.DeleteModel(
            name='Guarnicion',
        ),
        migrations.DeleteModel(
            name='Postre',
        ),
        migrations.DeleteModel(
            name='Precio',
        ),
        migrations.DeleteModel(
            name='Refresco',
        ),
        migrations.DeleteModel(
            name='SalsaPasta',
        ),
    ]
