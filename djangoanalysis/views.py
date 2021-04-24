from django.shortcuts import render, HttpResponse
from education.models import Contact

def home(request):
    name=['a','b','c', 'd']
    context ={
        'name':name
    }
    return render(request, 'home.html', context)
