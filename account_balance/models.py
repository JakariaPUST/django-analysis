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





class tax(models.Model):
    tax_country=models.CharField(max_length=100, blank=True, null=True)
    tax_percentage=models.FloatField(blank=True, null=True, default=0)
    country_tax_field=models.CharField(max_length=100, blank=True, null=True,default=0)
    def __str__(self):
        return self.tax_country



class taxDetails(models.Model):
    user= user=models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    tax_amount=models.FloatField(default=0)
    tax_id=models.CharField(max_length=100)
    tax_pay_date=models.DateTimeField(auto_now=True)
    tax_info_law=models.CharField(max_length=155, blank=True, null=True)
    tax_given_area=models.CharField(max_length=100,blank=True, null=True)
    tax_medium=models.CharField(max_length=100, blank=True, null=True)
    tax_description=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.tax_id