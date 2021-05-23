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



class Location(models.Model):
    latitude = models.FloatField(null=True, default=None, verbose_name="location latitude")
    longitude = models.FloatField(null=True, default=None, verbose_name="location longitude")
    street = models.CharField(max_length=100, verbose_name="street")
    zip_code = models.CharField(max_length=100, verbose_name="zip code")
    city = models.CharField(max_length=100, verbose_name="city")
    country = models.CharField(max_length=100, verbose_name="country")


class Sehir(models.Model):
    sehirAdi = models.CharField(max_length = 30,null=False,blank=False, verbose_name="Şehir Adı")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.sehirAdi
    class Meta:
        ordering = ['-sehirAdi']

class Ilce(models.Model):
    sehir = models.ForeignKey(Sehir,on_delete = models.CASCADE,related_name="SehirIlce")
    ilceAdi = models.CharField(max_length = 30,null=False,blank=False, verbose_name="İlçe Adı")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.ilceAdi
    class Meta:
        ordering = ['-eklenmeTarihi']

class Mahalle(models.Model):
    ilce = models.ForeignKey(Ilce,on_delete = models.CASCADE,related_name="MahalleIlce")
    mahalleAdi = models.CharField(max_length = 30,null=False,blank=False, verbose_name="Mahalle Adı")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.mahalleAdi
    class Meta:
        ordering = ['-eklenmeTarihi']

class Sokak(models.Model):
    mahalle = models.ForeignKey(Mahalle,on_delete = models.CASCADE,related_name="SokakMahalle")
    sokakAdi = models.CharField(max_length = 30,null=False,blank=False, verbose_name="Sokak Adı")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.sokakAdi
    class Meta:
        ordering = ['-eklenmeTarihi']

class Cadde(models.Model):
    sokak = models.ForeignKey(Sokak,on_delete = models.CASCADE,related_name="CaddeSokak")
    caddeAdi = models.CharField(max_length = 30,null=False,blank=False, verbose_name="Cadde Adı")
    eklenmeTarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.caddeAdi
    class Meta:
        ordering = ['-eklenmeTarihi']

class SaglikKuruluslari(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Ekleyen")
    kurulusAdi = models.CharField(max_length = 50,null=False,blank=False,verbose_name = "Kuruluş Adı")
    kurulusTuru =models.CharField(max_length=20,null=False,blank=False, choices=kurulusTurleri, verbose_name = "Kuruluş Türü")
    durum =models.CharField(max_length = 20,null=False,blank=False, choices=durumlar, verbose_name = "Durum")
    sehir = models.ForeignKey(Sehir,null=True, on_delete = models.CASCADE,related_name="SaglikKurulusSehir")
    ilce = models.ForeignKey(Ilce,null=True, on_delete = models.CASCADE,related_name="SaglikKurulusIlce")
    mahalle = models.ForeignKey(Mahalle,null=True, on_delete = models.CASCADE,related_name="SaglikKurulusMahalle")
    sokak = models.ForeignKey(Sokak,null=True, on_delete = models.CASCADE,related_name="SaglikKurulusSokak")
    cadde = models.ForeignKey(Cadde,null=True, on_delete = models.CASCADE,related_name="SaglikKurulusCadde")
    kapiNo = models.PositiveIntegerField(null=True,verbose_name = "Kapı No")
    tamAdres = models.CharField(max_length = 250,null=True,verbose_name = "Tam Adres")
    postaKodu = models.PositiveIntegerField(null=True,verbose_name = "Posta Kodu")
    enlem = models.FloatField(max_length = 50,null=False,blank=False,verbose_name = "Enlem")
    boylam = models.FloatField(max_length = 50,null=False,blank=False,verbose_name = "Boylam")
    telefon = models.PositiveIntegerField(null=False,blank=False,verbose_name = "Telefon")
    fax = models.PositiveIntegerField(verbose_name = "Fax")
    website = models.CharField(max_length = 50,verbose_name = "Website")
    mail = models.EmailField(max_length = 50,verbose_name = "Mail")
    doktorSayisi = models.PositiveIntegerField(verbose_name = "Doktor Sayısı")
    kisiUzaklik = models.FloatField(max_length = 500,null= True, verbose_name="Kişiye Olan Uzaklık")
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
    #memleket = models.CharField(max_length = 50,verbose_name = "LinkedIn")
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


class UserExtra(models.Model):
    user= models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    latitude = models.FloatField(null=True, default=None, verbose_name="Enlem")
    longitude = models.FloatField(null=True, default=None, verbose_name="Boylam")
    seviye = models.ForeignKey(Seviyeler, null=True ,on_delete = models.CASCADE,related_name="UserExtraSeviye")
    def __str__(self):
        return self.user

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



