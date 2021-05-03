from django.urls import path
from .views import *
app_name='multivalue_submit'
urlpatterns = [
	path('home2/', home2, name="home2"),
]

# multivalue_submit/home2/
