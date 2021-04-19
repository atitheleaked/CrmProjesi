# Generated by Django 3.2 on 2021-04-19 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hizmetler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hizmetAdi', models.CharField(max_length=50, verbose_name='Hizmet Adı')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='Kisiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50, verbose_name='Ad')),
                ('soyad', models.CharField(max_length=50, verbose_name='Soyad')),
                ('gorev', models.CharField(max_length=50, verbose_name='Gorev')),
                ('telefon', models.PositiveIntegerField(verbose_name='Telefon')),
                ('mail', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('linkedin', models.CharField(max_length=50, verbose_name='LinkedIn')),
                ('whatsapp', models.CharField(max_length=50, verbose_name='Whatsapp')),
                ('instagram', models.CharField(max_length=50, verbose_name='Instagram')),
                ('memleket', models.CharField(max_length=50, verbose_name='LinkedIn')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='Notlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notTur', models.CharField(choices=[('Istek', 'Istek'), ('Sikayet', 'Sikayet'), ('Oneri', 'Oneri')], max_length=20, verbose_name='Not Türü')),
                ('notIcerik', models.CharField(max_length=1000, verbose_name='Not')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='Personeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50, verbose_name='Ad')),
                ('soyad', models.CharField(max_length=50, verbose_name='Soyad')),
                ('mail', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('telefon', models.PositiveIntegerField(verbose_name='Telefon')),
                ('sifre', models.CharField(max_length=15, verbose_name='Parola')),
                ('dogumTarihi', models.DateField(verbose_name='Doğum Tarihi')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='SaglikKuruluslari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurulusAdi', models.CharField(max_length=50, verbose_name='Kuruluş Adı')),
                ('kurulusTuru', models.CharField(choices=[('Dis Polikinigi', 'Dis Polikinigi'), ('Ozel Hastane', 'Ozel Hastane'), ('Kamu Hastanesi', 'Kamu Hastanesi'), ('Estetik Hekimler', 'Estetik Hekimler'), ('IFV', 'IFV')], max_length=20, verbose_name='Kuruluş Türü')),
                ('durum', models.CharField(choices=[('Potansiyel', 'Potansiyel'), ('Yeni', 'Yeni'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Not Working', 'Not Working')], max_length=20, verbose_name='Durum')),
                ('enlem', models.FloatField(max_length=50, verbose_name='Enlem')),
                ('boylam', models.FloatField(max_length=50, verbose_name='Boylam')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ekleyen')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='Seviyeler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seviyeAdi', models.CharField(max_length=50, verbose_name='Seviye Adı')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='Uzmanliklar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uzmanlikAdi', models.CharField(max_length=50, verbose_name='Tedavi Adı')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='Tedaviler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tedaviAdi', models.CharField(max_length=50, verbose_name='Tedavi Adı')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('uzmanlikID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TedavilerUzmanlikID', to='base.uzmanliklar')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='SaglikTedaviler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('saglikID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SaglikTedavilerSaglikID', to='base.saglikkuruluslari')),
                ('tedaviID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SaglikTedavilerTedaviID', to='base.tedaviler')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='SaglikNotlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('notlID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SaglikNotlarSaglikID', to='base.notlar')),
                ('sagliklID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SaglikNotlarSaglikID', to='base.saglikkuruluslari')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='SaglikKisiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('kisiID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKisilerKisiID', to='base.kisiler')),
                ('saglikID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SaglikKisilerSaglikID', to='base.saglikkuruluslari')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='SaglikHizmetler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('hizmetID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.hizmetler')),
                ('kurulus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SaglikHizmetlerKurulus', to='base.saglikkuruluslari')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='PersonelSaglik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('personelID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PersonelSaglikPersonelID', to='base.personeller')),
                ('saglikID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PersonelSaglikSaglikID', to='base.saglikkuruluslari')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.AddField(
            model_name='personeller',
            name='seviye',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PersonellerSeviye', to='base.seviyeler'),
        ),
        migrations.AddField(
            model_name='notlar',
            name='personelID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NotlarPersonelID', to='base.personeller'),
        ),
        migrations.CreateModel(
            name='Mesajlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesaj', models.CharField(max_length=250, verbose_name='Mesaj')),
                ('okundu', models.BooleanField(default=False, verbose_name='Okundu')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('alıcı', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='MesajAlıcı')),
                ('gonderen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MesajGonderıcı', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.CreateModel(
            name='KisiNotlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('kisiID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='KisiNotlarKisiID', to='base.kisiler')),
                ('notID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='KisiNotlarNotId', to='base.notlar')),
            ],
            options={
                'ordering': ['-eklenmeTarihi'],
            },
        ),
        migrations.AddField(
            model_name='hizmetler',
            name='SaglikHizmet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HizmetlerSaglikHizmet', to='base.saglikkuruluslari'),
        ),
    ]
