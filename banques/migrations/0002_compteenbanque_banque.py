# Generated by Django 5.1.2 on 2024-10-24 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banques', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compteenbanque',
            name='banque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comptes', to='banques.banque'),
        ),
    ]