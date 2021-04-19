from django import forms
from .models import *


class MesajlarForm(forms.ModelForm):

    class Meta:
        model = Mesajlar
        fields = '__all__'
    

class SaglikKuruluslariForm(forms.ModelForm):
    class Meta:
        model = SaglikKuruluslari
        fields = '__all__'

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