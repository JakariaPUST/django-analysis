
from django.urls import path
from .views import contact, postview, postcreate, subjectview


urlpatterns = [
    path('contact/', contact, name="contact"),
    path('post/', postview , name="post"),
    path('create/', postcreate , name="create"),
    path('subject/', subjectview , name="subject"),
]
