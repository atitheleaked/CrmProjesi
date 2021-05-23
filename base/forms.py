from django import forms
from django.contrib.auth.models import User
from .models import *


class KullaniciDetayForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'is_superuser',
            'is_active'
        ]

class UserExtraForm(forms.ModelForm):

    class Meta:
        model = UserExtra
        fields = ['latitude','longitude']

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'

class MesajlarForm(forms.ModelForm):

    class Meta:
        model = Mesajlar
        fields = '__all__'

class SaglikKuruluslariFullForm(forms.ModelForm):
    class Meta:
        model = SaglikKuruluslari
        fields = [
            'kurulusAdi',
            'telefon',
            'kurulusTuru',
            'durum',
            'sehir',
            'ilce',
            'mahalle',
            'sokak',
            'cadde',
            'kapiNo',
            'postaKodu',
            'enlem',
            'boylam',
            'fax',
            'website',
            'mail',
            'doktorSayisi']


class SaglikKuruluslariForm(forms.ModelForm):
    class Meta:
        model = SaglikKuruluslari
        fields = [
            'kurulusAdi',
            'telefon',
            'kurulusTuru',
            'durum',
            'enlem',
            'boylam',
            'fax',
            'website',
            'mail',
            'doktorSayisi']

class SaglikHizmetlerForm(forms.ModelForm):
    class Meta:
        model = SaglikHizmetler
        fields = '__all__'

class HizmetlerForm(forms.ModelForm):
    class Meta:
        model = Hizmetler
        fields = '__all__'

class KisilerForm(forms.ModelForm):
    class Meta:
        model = Kisiler
        fields = '__all__'

class SaglikKisilerForm(forms.ModelForm):
    class Meta:
        model = SaglikKisiler
        fields = '__all__'

class UzmanliklarForm(forms.ModelForm):
    class Meta:
        model = Uzmanliklar
        fields = '__all__'

class TedavilerForm(forms.ModelForm):
    class Meta:
        model = Tedaviler
        fields = '__all__'

class SaglikTedavilerForm(forms.ModelForm):
    class Meta:
        model = SaglikTedaviler
        fields = '__all__'

class SeviyelerForm(forms.ModelForm):
    class Meta:
        model = Seviyeler
        fields = '__all__'

class PersonellerForm(forms.ModelForm):
    class Meta:
        model = Personeller
        fields = '__all__'
        

class NotlarForm(forms.ModelForm):
    class Meta:
        model = Notlar
        fields = '__all__'
    
class KisiNotlarForm(forms.ModelForm):
    class Meta:
        model = KisiNotlar
        fields = '__all__'

class SaglikNotlarForm(forms.ModelForm):
    class Meta:
        model = SaglikNotlar
        fields = '__all__'

class PersonelSaglikForm(forms.ModelForm):
    class Meta:
        model = PersonelSaglik
        fields = '__all__'