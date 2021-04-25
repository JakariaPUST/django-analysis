from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Contact,Post, Subject
from .forms import ContactForm, PostForm
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url='/' #or i can write like after form-invalid functions
    def form_valid(self, form):
        form.save()
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
        context['msg']="this is post list"
        return context

class postDetailView(DetailView):
    template_name = "education/postdetail.html"
    model=Post
    context_object_name="postdetail"
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        context['posts']=context.get('object_list')
        context['msg']="this is individual post"
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

        # form=PostForm(request.POST,request.FILES, initial=initials)
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            # sub=form.cleaned_data['subject']
            # for i in sub:
            #     obj.subject.add(i)
            #     obj.save()
            # class_in=form.cleaned_data['classs_in']
            # for i in class_in:
            #     obj.class_in.add(i)
            #     obj.save()
            # return HttpResponse("Success")
            
    else:
        # form= PostForm(initial=initials)
        form= PostForm()
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

