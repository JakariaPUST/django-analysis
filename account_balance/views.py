from django.shortcuts import render
from .models import Account, withdraw
# Create your views here.


def accountBalanceCalculation(request):
    acc=Account.objects.all()
    for i in acc:
        obj=Account.objects.get(id=i.id)
        pur=i.purchase_amnt
        ref=i.ref_amnt
        prantic=i.prantic_amnt
        middle=i.middle_amnt
        ehp=i.ehp_amnt
        esp=i.esp_amnt
        incentive=i.incentive_amnt
        totalamnts=(incentive+esp+ehp+middle+prantic+ref+pur)


        obj.total_amnt_WoP=totalamnts
        obj.save()

        # acc=Account.objects.filter(user__id=request.user.id).first()
        # objdel =  withdraw.objects.all().delete()
        obj2=withdraw()
        obj2.account=obj
        obj2.user= i.user
        obj2.prev_amnt= totalamnts
        obj2.current_amnt= totalamnts
        obj2.save()


    return render(request,'account_balance/show.html')


def withdrawView(request):
    obj=withdraw.objects.filter(user__id=request.user.id).first()

    requisation_amnt=30
    transaction_id='1kfTxx56jlj'
    print(request.user.id)


    # obj=withdraw()
    # obj.account=acc
    # obj.user= request.user
    obj.transaction_id = transaction_id
    temp_amt = obj.total_cashout_amnt + requisation_amnt
    obj.total_cashout_amnt= temp_amt
    obj.current_amnt= obj.prev_amnt - temp_amt
    obj.save()


    return render(request,'account_balance/withdraw.html')