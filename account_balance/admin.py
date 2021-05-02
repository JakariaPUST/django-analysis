from django.contrib import admin
from .models import Account, withdraw, tax, taxDetails
# Register your models here.
admin.site.register(Account)
admin.site.register(withdraw)
admin.site.register(tax)
admin.site.register(taxDetails)



