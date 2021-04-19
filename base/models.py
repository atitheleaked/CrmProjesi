from django.db import models
from ckeditor.fields import RichTextField
from django import forms
from django.conf import settings

# Create your models here.

kurulusTurleri = (
        ('Dis Polikinigi', 'Dis Polikinigi'),
        ('Ozel Hastane', 'Ozel Hastane'),
        ('Kamu Hastanesi', 'Kamu Hastanesi'),
        ('Estetik Hekimler', 'Estetik Hekimler'),
        ('IFV', 'IFV'),
    )
durumlar = (
        ('Potansiyel', 'Potansiyel'),
        ('Yeni', 'Yeni'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Not Working', 'Not Working'),
    )
notTurleri = (
        ('Istek', 'Istek'),
        ('Sikayet', 'Sikayet'),
        ('Oneri', 'Oneri'),
    )



class SaglikKuruluslari(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Ekleyen")
    kurulusAdi = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Kuruluş Adı")
    kurulusTuru =models.CharField(max_length=20,null=False,blank=False, choices=kurulusTurleri, verbose_name = "Kuruluş Türü")
    durum =models.CharField(max_length = 20,null=False,blank=False, choices=durumlar, verbose_name = "Durum")
    #sehir = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Şehir")
    #ilce = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "İlçe")
    #mahalle = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Mahalle")
    ### DEĞİŞECEK
    #sokak = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Sokak")
    ###
    #cadde = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Cadde")
    #kapıNo = models.PositiveIntegerField(null=False,blank=False,verbose_name = "Kapı No")
    #tamAdres = models.CharField(max_length = 150,null=False,blank=False,verbose_name = "Tam Adres")
    #postaKodu = models.PositiveIntegerField(null=False,blank=False,verbose_name = "Posta Kodu")
    enlem = models.FloatField(max_length = 50,null=False,blank=False,verbose_name = "Enlem")
    boylam = models.FloatField(max_length = 50,null=False,blank=False,verbose_name = "Boylam")
    
    #telefon = models.PositiveIntegerField(null=False,blank=False,verbose_name = "Telefon")
    #fax = models.PositiveIntegerField(null=False,blank=False,verbose_name = "Fax")
    #website = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Website")
    #mail = models.EmailField(max_length = 50,null=False,blank=False,verbose_name = "Mail")
    #doktorSayisi = models.PositiveIntegerField(null=False,blank=False,verbose_name = "Doktor Sayısı")
    #kurulusNotu = models.CharField(verbose_name="Yorumunuz.. (En fazla 1000 karakter)",null=True,max_length=1000)
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.kurulusAdi
    class Meta:
        ordering = ['-eklenmeTarihi']
    

class Hizmetler(models.Model):
    SaglikHizmet = models.ForeignKey(SaglikKuruluslari,on_delete = models.CASCADE,related_name="HizmetlerSaglikHizmet")
    hizmetAdi = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Hizmet Adı")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.hizmetAdi
    class Meta:
        ordering = ['-eklenmeTarihi']


class SaglikHizmetler(models.Model):
    kurulus = models.ForeignKey(SaglikKuruluslari,on_delete = models.CASCADE,related_name="SaglikHizmetlerKurulus")
    hizmetID = models.ForeignKey(Hizmetler, on_delete = models.CASCADE)
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.kurulus
    class Meta:
        ordering = ['-eklenmeTarihi']


class Kisiler(models.Model):
    ad = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Ad")
    soyad = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Soyad")
    gorev = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Gorev")
    telefon = models.PositiveIntegerField(null=False,blank=False,verbose_name = "Telefon")
    mail = models.EmailField(max_length = 50,null=False,blank=False,verbose_name = "E-mail")
    linkedin = models.CharField(max_length = 50,verbose_name = "LinkedIn")
    whatsapp = models.CharField(max_length = 50,verbose_name = "Whatsapp")
    instagram = models.CharField(max_length = 50,verbose_name = "Instagram")

    ## DEĞİŞECEK
    memleket = models.CharField(max_length = 50,verbose_name = "LinkedIn")
    ##
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.ad
    class Meta:
        ordering = ['-eklenmeTarihi']


class SaglikKisiler(models.Model):
    saglikID = models.ForeignKey(SaglikKuruluslari,on_delete = models.CASCADE,related_name="SaglikKisilerSaglikID")
    kisiID = models.ForeignKey(Kisiler,on_delete = models.CASCADE,related_name="SaglikKisilerKisiID")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.saglikID
    class Meta:
        ordering = ['-eklenmeTarihi']


class Uzmanliklar(models.Model):
    uzmanlikAdi = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Tedavi Adı")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.uzmanlikAdi
    class Meta:
        ordering = ['-eklenmeTarihi']


class Tedaviler(models.Model):
    tedaviAdi = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Tedavi Adı")
    uzmanlikID = models.ForeignKey(Uzmanliklar,on_delete = models.CASCADE,related_name="TedavilerUzmanlikID")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.tedaviAdi
    class Meta:
        ordering = ['-eklenmeTarihi']


class SaglikTedaviler(models.Model):
    saglikID = models.ForeignKey(SaglikKuruluslari,on_delete = models.CASCADE,related_name="SaglikTedavilerSaglikID")
    tedaviID = models.ForeignKey(Tedaviler,on_delete = models.CASCADE,related_name="SaglikTedavilerTedaviID")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.saglikID
    class Meta:
        ordering = ['-eklenmeTarihi']


class Seviyeler(models.Model):
    seviyeAdi = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Seviye Adı")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.seviyeAdi
    class Meta:
        ordering = ['-eklenmeTarihi']


class Personeller(models.Model):
    ad = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Ad")
    soyad = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Soyad")
    mail = models.EmailField(max_length = 50,null=False,blank=False,verbose_name = "E-mail")
    telefon = models.PositiveIntegerField(null=False,blank=False,verbose_name = "Telefon")
    sifre = models.CharField(max_length = 15,null=False,blank=False,verbose_name = "Parola")
    seviye = models.ForeignKey(Seviyeler,on_delete = models.CASCADE,related_name="PersonellerSeviye")
    dogumTarihi = models.DateField(verbose_name="Doğum Tarihi")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.ad
    class Meta:
        ordering = ['-eklenmeTarihi']


class Notlar(models.Model):
    personelID = models.ForeignKey(Personeller,on_delete = models.CASCADE,related_name="NotlarPersonelID")
    notTur = models.CharField(max_length=20,null=False,blank=False, choices=notTurleri, verbose_name = "Not Türü")
    notIcerik = models.CharField(max_length=1000,null=False,blank=False,verbose_name="Not")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.personelID.ad
    class Meta:
        ordering = ['-eklenmeTarihi']



class KisiNotlar(models.Model):
    kisiID = models.ForeignKey(Kisiler,on_delete = models.CASCADE,related_name="KisiNotlarKisiID")
    notID = models.ForeignKey(Notlar,on_delete = models.CASCADE,related_name="KisiNotlarNotId")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.kisiID
    class Meta:
        ordering = ['-eklenmeTarihi']


class SaglikNotlar(models.Model):
    sagliklID = models.ForeignKey(SaglikKuruluslari,on_delete = models.CASCADE,related_name="SaglikNotlarSaglikID")
    notlID = models.ForeignKey(Notlar,on_delete = models.CASCADE,related_name="SaglikNotlarSaglikID")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.saglikID
    class Meta:
        ordering = ['-eklenmeTarihi']



class PersonelSaglik(models.Model):
    personelID = models.ForeignKey(Personeller,on_delete = models.CASCADE,related_name="PersonelSaglikPersonelID")
    saglikID = models.ForeignKey(SaglikKuruluslari,on_delete = models.CASCADE,related_name="PersonelSaglikSaglikID")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.saglikID
    class Meta:
        ordering = ['-eklenmeTarihi']


class Mesajlar(models.Model):
    gonderen = models.ForeignKey("auth.User",on_delete = models.CASCADE,related_name="MesajGonderıcı")
    alıcı = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "MesajAlıcı")
    mesaj = models.CharField(max_length=250,verbose_name = "Mesaj")
    okundu = models.BooleanField(default=False, verbose_name="Okundu")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.mesaj
    class Meta:
        ordering = ['-eklenmeTarihi']



