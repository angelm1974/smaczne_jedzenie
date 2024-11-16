# Generated by Django 5.1.3 on 2024-11-16 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producent',
            options={'verbose_name': 'Producent', 'verbose_name_plural': 'Producenci'},
        ),
        migrations.CreateModel(
            name='Surowiec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=64)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('jednostka', models.CharField(max_length=64)),
                ('producent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.producent')),
            ],
            options={
                'verbose_name': 'Surowiec',
                'verbose_name_plural': 'Surowce',
            },
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=64)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('opis', models.TextField()),
                ('producent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.producent')),
                ('surowce', models.ManyToManyField(to='jedzonko.surowiec')),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
        ),
    ]