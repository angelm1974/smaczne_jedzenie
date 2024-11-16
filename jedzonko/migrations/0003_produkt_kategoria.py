# Generated by Django 5.1.3 on 2024-11-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0002_alter_producent_options_surowiec_produkt'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='kategoria',
            field=models.CharField(choices=[('napoje', 'napoje'), ('słodycze', 'słodycze'), ('posiłki', 'posiłki'), ('owoce', 'owoce')], default='posiłki', max_length=64),
        ),
    ]