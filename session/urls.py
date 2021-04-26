
from django.urls import path
from .views import loginuser, logoutuser, registration, changepassword, activate
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/',loginuser , name="login"),
    path('logout/',logoutuser , name="logout"),
    path('signup/',registration , name="signup"),
    path('changepass/',changepassword , name="changepass"),
    path('activate/<uidb64>/<token>/',activate,name="activate"),


    path('reset/password/',PasswordResetView.as_view(template_name='session/reset_pass.html'),name="password_reset"),
    path('reset/password/done/',PasswordResetDoneView.as_view(template_name='session/reset_pass_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='session/reset_pass_confirm.html'),name="password_reset_confirm"),
    path('reset/done/',PasswordResetView.as_view(template_name='session/reset_pass_complete.html'),name="password_reset_complete"),

]
