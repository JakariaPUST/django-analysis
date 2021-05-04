from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from account_balance.models import Account
from .forms import withdrawForm
from django.urls import reverse

# Create your views here.
def WithdrawView(request):
    # print(request.user.id)
    if request.user.id==None:
        # return Redirect(login)
        return redirect(reverse('login'))


    p = Account.objects.filter(id=1).first()
    if request.method == "POST":
        form=withdrawForm(request.POST)
        if form.is_valid():
            requisation_amnt=form.cleaned_data['requisition']
            print("Jakariar biye")
            print(requisation_amnt)
            form=withdrawForm()
        else:
            print("Cunnur cap")
    else:
        form=withdrawForm()

    context = {
        'form': form
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