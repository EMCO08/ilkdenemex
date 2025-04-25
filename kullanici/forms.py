from django import forms
from .models import Kullanici
from django.forms.widgets import DateInput

class KullaniciForm(forms.ModelForm):
    class Meta:
        model = Kullanici
        fields = ['isim', 'dogum_tarihi', 'profil_resmi']
        widgets = {
            'dogum_tarihi': DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'isim': 'İsim',
            'dogum_tarihi': 'Doğum Tarihi',
            'profil_resmi': 'Profil Resmi',
        } 