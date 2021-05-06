from django import forms
# from django.contrib.auth.models import User

from .models import Withdraw


class withdrawForm(forms.ModelForm):
    requisition = forms.FloatField(required=True)
    class Meta:
        model = Withdraw
        fields = ['requisition']


class Raw_withdrawForm(forms.Form):
    requisition = forms.FloatField(required=True)

 