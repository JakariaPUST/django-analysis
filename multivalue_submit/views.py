from django.shortcuts import render
from .models import Todo

# Create your views here.
def home2(request):
    context={}
    if request.method == 'POST':
        task=request.POST.get('task')
        task= task+str(" nazmul")
        print(task)
        context={ 'name': task }
        new = Todo(task=task)
        new.save()
    return render(request,"form.html",context)
