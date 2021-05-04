from django.urls import path,include
from .views import WithdrawView
app_name = 'api_transaction'
urlpatterns = [
    path('',WithdrawView, name='withdraw_index'),
]

# 127.0.0.1:8000/transaction/