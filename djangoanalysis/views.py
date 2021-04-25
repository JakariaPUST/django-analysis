from django.shortcuts import render, HttpResponse
from education.models import Contact
from django.views.generic import TemplateView

# def home(request):
#     name=['a','b','c', 'd']
#     context ={
#         'name':name
#     }
#     return render(request, 'home.html', context)
class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["msg"] = "welcome to website"
        context["msg2"] = "welcome to website again"
        return context
    