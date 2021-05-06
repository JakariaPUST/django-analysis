from django.db import models
from django.contrib.auth.models import User

class Office_Person(models.Model):
    name = models.CharField(max_length=250)
    designation_date = models.DateTimeField()
    designationID = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=16)
    birth_date = models.DateField(max_length=30)
    

class TaxPeriodType(models.Model):
    period_type = models.CharField(max_length=100)
    period_duration = models.PositiveIntegerField()
    
    def __str__(self):
        return self.period_type



class TaxSetup(models.Model):
    name_of_field = models.CharField(max_length=500)
    country = models.CharField(max_length=250) # fk Country
    percentage = models.FloatField()

    def __str__(self):
        return self.country+"-"+self.name_of_field

# Create your models here.
class Withdraw(models.Model):
    date = models.DateTimeField()
    requisition = models.FloatField()
    tax = models.FloatField(default=0)
    vat = models.FloatField(default=0)
    transaction_cost = models.FloatField(default=0)
    user = models.ForeignKey(User,related_name='usr', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Tax(models.Model):
    withdraw = models.OneToOneField(Withdraw, related_name='wthdrw', on_delete=models.CASCADE)
    cashout_amt = models.FloatField(default=0)
    tax_paid_amt = models.FloatField(blank=True, null=True)
    taxID = models.CharField(max_length=500, blank=True, null=True)
    tax_paid_date = models.DateTimeField(blank=True, null=True)
    # tax_paid_amt = models.FloatField(blank=True, null=True)
    tax_info_law = models.TextField(blank=True, null=True)
    tax_given_area = models.TextField(blank=True, null=True)
    tax_medium = models.CharField(max_length=500,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    user = models.ForeignKey(User,related_name='tax_usr', on_delete=models.CASCADE)
    taxperiodtype = models.ForeignKey(TaxPeriodType, blank=True, null=True, on_delete=models.SET_NULL) 
    created_office_person = models.ForeignKey(Office_Person, blank=True, null=True, on_delete=models.SET_NULL) 

