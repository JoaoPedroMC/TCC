# Generated by Django 4.1.2 on 2022-10-31 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_coviddados_casos_recuperados'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CovidDados',
        ),
    ]