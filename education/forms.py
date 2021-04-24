from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(max_length=100, label="Your name")
    email= forms.CharField(max_length=100, label="Your email")
    phone= forms.CharField(max_length=100, label="Your phone")
    content= forms.CharField(max_length=100, label="Your details")