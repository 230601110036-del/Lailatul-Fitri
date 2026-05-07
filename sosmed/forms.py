from django import forms
from .models import Instagram

# usages
class InstagramForm(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = [
            'nama_depan',
            'nama_belakang',
            'username',
        ]