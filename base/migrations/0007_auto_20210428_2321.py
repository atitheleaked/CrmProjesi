# Generated by Django 3.2 on 2021-04-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_saglikkuruluslari_kapino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saglikkuruluslari',
            name='postaKodu',
            field=models.PositiveIntegerField(null=True, verbose_name='Posta Kodu'),
        ),
        migrations.AlterField(
            model_name='saglikkuruluslari',
            name='tamAdres',
            field=models.CharField(max_length=250, null=True, verbose_name='Tam Adres'),
        ),
    ]
