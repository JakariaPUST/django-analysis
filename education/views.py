from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from .models import Contact,Post, Subject, Classs_in, Comment, District
from .forms import ContactForm, PostForm
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
import requests
import json
from django.http import HttpResponseRedirect

from .templatetags import tag





class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url='/' #or i can write like after form-invalid functions
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Form Successfully submitted')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('home')


# class ContactView(View):
#     form_class = ContactForm
#     template_name = 'contact.html'
#     def get(self, request, *args, **kwargs):
#         form =self.form_class()
#         return render(request, self.template_name, {'form':form})


#     def post(self, request, *args, **kwargs):
#         form =self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("SUCCESS")
#         return render (request, self.template_name, {'form':form})


# Create your views here.
# def contact(request):
#     if request.method == "POST":
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form= ContactForm()

#     return render(request, 'contact.html', {'form':form})



class postView(ListView):
    template_name = "education/postlist.html"
    model=Post
    context_object_name="posts"
    # queryset= Post.objects.filter(user=1)
    queryset= Post.objects.all()
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        context['posts']=context.get('object_list')
        # context['msg']="this is post list"
        context['subjects']= Subject.objects.all()
        context['classes']= Classs_in.objects.all()
        return context

class postDetailView(DetailView):
    template_name = "education/postdetail.html"
    model=Post
    context_object_name="postdetail"
   
    def get_context_data(self, *args, **kwargs):
        self.object.views.add(self.request.user)
        liked=False
        if self.object.likes.filter(id=self.request.user.id).exists():
            liked=True

        context=super().get_context_data(*args, **kwargs)
        post=context.get('object')
        comments=Comment.objects.filter(post=post.id, parent=None)
        replies=Comment.objects.filter(post=post.id).exclude(parent=None)
        DictofReply={}
        for reply in replies:
            if reply.parent.id not in DictofReply.keys():
                DictofReply[reply.parent.id]=[reply]
            else:
                DictofReply[reply.parent.id].append(reply)
        
        context['post']= context.get('object')
        context['liked']= liked
        context['comments']= comments
        context['DictofReply']= DictofReply
        return context


def postview(request):
    post=Post.objects.all()

    return render(request, 'education/post.html', {'post':post})

def subjectview(request):
    subject=Subject.objects.get(name='English')
    subpost=subject.subject_set.all()

    return render(request, 'education/subjectview.html', {'subject':subject, 'subpost':subpost})

def postcreate(request):
    # initials={
    # 'title':"My Title is",
    # 'email':"jakaria.pust@",
    # 'salary':"2000",
    # 'details':"My Though is"}
    if request.method == "POST":

        form=PostForm(request.POST,request.FILES )
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            dis=form.cleaned_data['district']
            if not District.objects.filter(name=dis).exists():
                disobj=District(name=dis)
                disobj.save()
            sub=form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in=form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("Success")
            
    else:
        # form= PostForm(initial=initials)
        form=PostForm(district_set=District.objects.all().order_by('name'))
    return render(request, 'education/postcreate.html', {'form':form})




class postEditView(UpdateView):
    model=Post
    form_class = PostForm
    context_object_name="postedit"
    template_name = "education/postcreate.html"
    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('education:postdetail', kwargs={'pk':id})

class postDeleteView(DeleteView):
    model=Post
    context_object_name="postdelete"
    template_name = "education/postdelete.html"
    success_url=reverse_lazy('education:postlist')

def searchresult(request):
    query=request.POST.get('search', '')
    if query:
        queryset=(Q(title__icontains=query)) | (Q(category__icontains=query)) | (Q(medium__icontains=query)) | (Q(subject__name__icontains=query))| (Q(details__icontains=query))
        results=Post.objects.filter(queryset).distinct()
    else:
        results=[]
    context ={
        'results': results
    }
    return render (request, 'education/search.html', context)
def filter(request):
    if request.method=="POST":
        subject = request.POST['subject']
        class_in = request.POST['classs_in']
        salary_from = request.POST['salary_from']
        salary_to = request.POST['salary_to']
        available = request.POST['available']

        if subject or class_in:
            queryset= (Q(subject__name__icontains=subject)) & (Q(class_in__name__icontains=class_in))
            results=Post.objects.filter(queryset).distinct()

            if available:
                results=results.filter(available=True)

            if salary_from:
                results=results.filter(salary__gte=salary_from)

            if salary_to:
                results=results.filter(salary__lte=salary_to)

        else:
            results=[]
        context ={
            'results': results
        }
        return render (request, 'education/search.html', context)
            
    



# API INTEGRATION
def postview(request):
    api_request= requests.get(f"https://jsonplaceholder.typicode.com/posts")
    try:
        api=json.loads(api_request.content)
    except:
        api="Error"
    return render(request,'education/postview.html',{'api':api})



# LIKE BUTTON FUNCTIONALITY

def likepost(request,id):
    if request.method=="POST":
        post=Post.objects.get(id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





# COMMENT FUNCTIONALITY

def addcomment(request):
    if request.method=="POST":
        comment=request.POST['comment']
        parentid=request.POST['parentid']
        postid=request.POST['postid']
        post=Post.objects.get(id=postid)
        if parentid:
            parent=Comment.objects.get(id=parentid)
            newcom= Comment(text=comment, user=request.user, post=post, parent=parent)
            newcom.save()
        else:
            newcom= Comment(text=comment, user=request.user, post=post)
            newcom.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



from .forms import  FileModelForm
from .models import PostFile
def addphoto(request, id):
    post=Post.objects.get(id=id)
    if request.method=="POST":
        form=FileModelForm(request.POST, request.FILES)
        if form.is_valid():
            image=form.cleaned_data['image']
            obj=PostFile(image=image, post=post)
            obj.save()
            messages.success(request, 'SUccessfully uploaded image')
            return redirect(f'/education/postdetail/{id}/')
    else:
        form=FileModelForm()
    context={
        'form':form,
        'id':id
    }
    return render(request,'education/addphoto.html',context)


    