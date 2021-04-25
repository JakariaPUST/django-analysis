from django.shortcuts import render
from .models import Contact,Post, Subject
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

def subjectview(request):
    subject=Subject.objects.get(name='English')
    subpost=subject.subject_set.all()

    return render(request, 'education/subjectview.html', {'subject':subject, 'subpost':subpost})

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