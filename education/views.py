from django.shortcuts import render
from .models import Contact,Post
from .forms import ContactForm, PostForm
# Create your views here.
def contact(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= ContactForm()

    return render(request, 'contact.html', {'form':form})


def postview(request):
    post=Post.objects.all()

    return render(request, 'education/post.html', {'post':post})

def postcreate(request):
    if request.method == "POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
    else:
        form= PostForm()
    return render(request, 'education/postcreate.html', {'form':form})