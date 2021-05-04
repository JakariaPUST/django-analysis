from django.shortcuts import render

# Create your views here.
def WithdrawView(request):
    
    return render(request, 'api_transaction/withdraw_index.html', context={})