from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from account_balance.models import Account
from .forms import withdrawForm
from django.urls import reverse
from .models import Withdraw, Tax
from account_balance.models import Account
from django.db.models import Count, Sum, Avg
import datetime
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your views here.
def WithdrawView(request):
    # print(request.user.id)
    if request.user.id==None:
        # return Redirect(login)
        return redirect(reverse('login'))

    usrID = request.user.id
    print(usrID)
    p = Account.objects.filter(user__id=usrID).first()
    print(p)
    t_amt = Account.Total_Amt(p) # total amt <-- Account
    print(t_amt)
    # withdraw_sum_amt = Withdraw.objects.filter(user__id=usrID).aggregate(Sum('requisition'))
    
    # balance = t_amt-withdraw_sum_amt['requisition__sum']
    withdraw_sum_amt = Withdraw.objects.filter(user__id=usrID).aggregate(Sum('requisition'))
    wd_total_amt = withdraw_sum_amt['requisition__sum']
    if wd_total_amt==None:
        wd_total_amt = 0
    balance = t_amt-wd_total_amt
    print(withdraw_sum_amt)

    if request.method == "POST":
        form=withdrawForm(request.POST)
        if form.is_valid():
            requisation_amnt= abs(form.cleaned_data['requisition'])

            balance_ck = wd_total_amt + requisation_amnt  
            print(balance_ck)
            purchase_percentage = (p.purchase_amnt*100)/Account.Total_Amt(p)

            if balance_ck<=t_amt and requisation_amnt >= 1 and purchase_percentage >= 10:

                # print("Jakariar biye")
                # print(requisation_amnt)
                wd = Withdraw()
                wd.requisition = requisation_amnt
                wd.date = timezone.now()
                # wd.tax = 0
                # wd.vat = 0
                # wd.transaction_cost = requisation_amnt * 0.05
                wd.user = request.user
                # wd.status = False
                tx = Tax()
                wd.save()
                tx.withdraw = wd
                tx.save()
                form=withdrawForm()
                # withdraw_sum_amt = Withdraw.objects.filter(user__id=usrID).aggregate(Sum('requisition'))
                # balance = t_amt-withdraw_sum_amt['requisition__sum']
            # print(withdraw_sum_amt)
            else:
                print("Sorry! You have not enough balance to withdraw.")

        else:

            print("Sorry! You have not enough balance to withdraw.")
            # form=withdrawForm()
    else:
        form=withdrawForm()
    
    
    pendint_withdraw_sum_amt = Withdraw.objects.filter(user__id=usrID, status=False).aggregate(Sum('requisition'))
    pendint_withdraw_sum_amt = pendint_withdraw_sum_amt['requisition__sum']
    withdraw_total_amt = Withdraw.objects.filter(user__id=usrID, status=True).aggregate(Sum('requisition'))
    withdraw_total_amt = withdraw_total_amt['requisition__sum']

    withdraw_sum_amt = Withdraw.objects.filter(user__id=usrID).aggregate(Sum('requisition'))
    wd_total_amt = withdraw_sum_amt['requisition__sum']
    if wd_total_amt==None:
        wd_total_amt = 0
    balance = t_amt-wd_total_amt
    print(withdraw_sum_amt)
    

    context = {
        'form': form,
        'balance': balance,
        'wd_total_amt': withdraw_total_amt,
        'pending_wd_amt': pendint_withdraw_sum_amt
    }
 
    return render(request, 'api_transaction/withdraw_index.html', context)



       
# from django.http import HttpResponseRedirect
# from django.shortcuts import render

# from .forms import NameForm

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})