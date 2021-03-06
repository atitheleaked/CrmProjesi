# Generated by Django 3.2 on 2021-04-28 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210427_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saglikkuruluslari',
            name='cadde',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusCadde', to='base.cadde'),
        ),
        migrations.AlterField(
            model_name='saglikkuruluslari',
            name='ilce',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusIlce', to='base.ilce'),
        ),
        migrations.AlterField(
            model_name='saglikkuruluslari',
            name='mahalle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusMahalle', to='base.mahalle'),
        ),
        migrations.AlterField(
            model_name='saglikkuruluslari',
            name='sehir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusSehir', to='base.sehir'),
        ),
        migrations.AlterField(
            model_name='saglikkuruluslari',
            name='sokak',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKurulusSokak', to='base.sokak'),
        ),
    ]
