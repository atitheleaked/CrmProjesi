# Generated by Django 3.2 on 2021-04-27 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210427_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='saglikkuruluslari',
            name='cadde',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusCadde', to='base.cadde'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saglikkuruluslari',
            name='ilce',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusIlce', to='base.ilce'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saglikkuruluslari',
            name='kapiNo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusKapiNo', to='base.kapino'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saglikkuruluslari',
            name='mahalle',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusMahalle', to='base.mahalle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saglikkuruluslari',
            name='postaKodu',
            field=models.PositiveIntegerField(default=0, verbose_name='Posta Kodu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saglikkuruluslari',
            name='sehir',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusSehir', to='base.sehir'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saglikkuruluslari',
            name='sokak',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusSokak', to='base.sokak'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saglikkuruluslari',
            name='tamAdres',
            field=models.CharField(default='', max_length=250, verbose_name='Tam Adres'),
            preserve_default=False,
        ),
    ]
