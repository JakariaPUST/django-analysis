from django.shortcuts import render, HttpResponse

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

        print(name)
        print(email)
        print(phone)
        print(content)

    return render(request, 'contact.html')