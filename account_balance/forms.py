from django import forms
from django.contrib.auth.models import User

from .models import Account, withdraw

class withdrawForm(forms.ModelForm):
    class Meta:
        model = withdraw
        fields = ['requisation_amnt']