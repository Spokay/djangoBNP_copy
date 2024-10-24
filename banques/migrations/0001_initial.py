# Generated by Django 5.1.2 on 2024-10-24 15:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('montant', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('TRANSACTION', 'Transaction'), ('DEPOT', 'Dépot'), ('RETRAIT', 'Retrait'), ('VIREMENT', 'Virement')], default='TRANSACTION', max_length=50, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='CompteEnBanque',
            fields=[
                ('compte_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('solde', models.FloatField(default=0.0)),
                ('taux_interet', models.FloatField(default=0.01)),
                ('pin', models.PositiveIntegerField(default=0)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comptes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('banque_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('utilisateurs', models.ManyToManyField(blank=True, related_name='banques', to=settings.AUTH_USER_MODEL)),
                ('comptes_bancaires', models.ManyToManyField(blank=True, related_name='banques', to='banques.compteenbanque')),
            ],
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='banques.transaction')),
            ],
            bases=('banques.transaction',),
        ),
        migrations.CreateModel(
            name='Retrait',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='banques.transaction')),
            ],
            bases=('banques.transaction',),
        ),
        migrations.AddField(
            model_name='transaction',
            name='compte_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_source', to='banques.compteenbanque'),
        ),
        migrations.CreateModel(
            name='Virement',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='banques.transaction')),
                ('compte_cible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_cible', to='banques.compteenbanque')),
            ],
            bases=('banques.transaction',),
        ),
    ]