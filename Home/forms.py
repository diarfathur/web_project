from django import forms
from .models import Koleksi

class AddNew(forms.ModelForm):
    class Meta:
        model = Koleksi
        fields = ('nama', 'gambar', 'user', 'tipe_koleksi')