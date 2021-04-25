
from django.urls import path
from .views import postview, postcreate, subjectview, ContactView
from .forms import ContactForm2

urlpatterns = [
    # path('contact/', contact, name="contact"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('contact2/', ContactView.as_view(form_class=ContactForm2, template_name="contact copy.html"), name="contact"),
    path('post/', postview , name="post"),
    path('create/', postcreate , name="create"),
    path('subject/', subjectview , name="subject"),
]
