
from django.urls import path
from .views import contact, postview, postcreate


urlpatterns = [
    path('contact/', contact, name="contact"),
    path('post/', postview , name="post"),
    path('create/', postcreate , name="create"),
]
