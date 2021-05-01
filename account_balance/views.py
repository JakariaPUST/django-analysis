from django.shortcuts import render
from .models import Account, withdraw
import datetime
from django.utils import timezone
# Create your views here.


def accountBalanceCalculation(request):
    acc=Account.objects.all()
    wd=withdraw.objects.all()
    wd.delete()
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


        purchase_percent= (pur/100)*totalamnts #calculation percentage of purchase commission
        print("--------------------- total pur---------------------")
        print(pur)

        print("--------------------- percase commissions percentage------------")
        print(purchase_percent)

        print("--------------------- total amnt---------------------")
        print(totalamnts)




        obj.total_amnt_WoP=totalamnts
        obj.save()

        # acc=Account.objects.filter(user__id=request.user.id).first()
        # objdel =  withdraw.objects.all().delete()
        obj2=withdraw()
        obj2.account=obj
        obj2.user= i.user
        obj2.prev_amnt= totalamnts
        # obj2.current_amnt= obj2.prev_amnt
        obj2.current_amnt= totalamnts


        obj2.prev_pur_tot = pur

        obj2.save()


    return render(request,'account_balance/show.html')


def withdrawView(request):
    obj=withdraw.objects.filter(user__id=request.user.id).first()

    

    requisation_amnt=30
    transaction_id='1kfTxx56jlj'

    # pur_per_amnt=10

    

    obj.transaction_id = transaction_id
    obj.requisation_amnt=requisation_amnt

    temp_amt = obj.total_cashout_amnt + requisation_amnt
    obj.total_cashout_amnt= temp_amt
    obj.current_amnt= obj.prev_amnt - temp_amt


    #pur_per_amnt  #it's calculation needed

    x = obj.prev_pur_tot
    print("---------------- purchase --------")
    
    pur_per_amnt= (10/100)* x
    print(pur_per_amnt)


    y = obj.cashout_pur_tot + pur_per_amnt
    obj.cashout_pur_tot =  y
    obj.current_pur_tot= x - y


    # obj.modified_at=timezone.now()
    obj.save()


    return render(request,'account_balance/withdraw.html')