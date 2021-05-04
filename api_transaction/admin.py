from django.contrib import admin
from .models import Office_Person, TaxPeriodType, TaxSetup, Withdraw, Tax
# Register your models here.
admin.site.register([Office_Person, TaxPeriodType, TaxSetup, Withdraw, Tax])
