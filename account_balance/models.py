from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Account(models.Model):
    purchase_amnt=models.FloatField()
    ref_amnt=models.FloatField()
    prantic_amnt=models.FloatField()
    middle_amnt=models.FloatField()
    ehp_amnt=models.FloatField()
    esp_amnt=models.FloatField()
    incentive_amnt=models.FloatField()
    user=models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    total_amnt_WoP= models.FloatField()


class withdraw(models.Model):
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    user=models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    prev_amnt=models.FloatField(blank=True, null=True, default=0)
    current_amnt=models.FloatField(blank=True, null=True, default=0)
    adjast_amnt=models.FloatField(blank=True, null=True, default=0)
    requisation_amnt=models.FloatField(blank=True, null=True, default=0)


    total_cashout_amnt=models.FloatField(default=0)
    transaction_id=models.CharField(max_length=100,blank=True, null=True)
    status=models.BooleanField(default=False)

    #purchase percentage
    prev_pur_tot=models.FloatField(blank=True, null=True, default=0)
    cashout_pur_tot=models.FloatField(default=0)
    current_pur_tot=models.FloatField(blank=True, null=True, default=0)

    # created_at=models.DateTimeField(default=now)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    # modified_at=models.DateTimeField("modified date")



