# Generated by Django 2.2.7 on 2019-11-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstaCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomEsci', models.CharField(max_length=50, verbose_name='Estado Civil')),
            ],
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombEtni', models.CharField(max_length=50, verbose_name='Grupo Etnico')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTiDo', models.CharField(max_length=50, verbose_name='Tipo de Documento')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTies', models.CharField(max_length=50, verbose_name='Tipo de Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Tipologr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTilo', models.CharField(max_length=50, verbose_name='Tipo de Logro')),
            ],
        ),
    ]
