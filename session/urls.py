
from django.urls import path
from education.views import postview, postcreate, subjectview, ContactView, postView, postDetailView, postEditView, postDeleteView, searchresult, filter
from education.forms import ContactForm2
from .views import loginuser, logoutuser
app_name='session'

urlpatterns = [
    path('login/',loginuser , name="login"),
    path('logout/',logoutuser , name="logout"),

]
