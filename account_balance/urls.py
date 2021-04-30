
from django.urls import path
from .views import accountBalanceCalculation, withdrawView

app_name='account_balance'

urlpatterns = [
    path('accntbal/', accountBalanceCalculation, name="accntbal"),
    path('withdraw/', withdrawView, name="withdraw"),
]


# http://127.0.0.1:8000/account_balance/accntbal/
# http://127.0.0.1:8000/account_balance/withdraw/