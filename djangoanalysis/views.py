from django.shortcuts import render, HttpResponse
from education.models import Contact

def home(request):
    name=['a','b','c', 'd']
    context ={
        'name':name
    }
    return render(request, 'home.html', context)

def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        obj = Contact(name=name, email=email, phone=phone, content=content)
        obj.save()

    return render(request, 'contact.html')