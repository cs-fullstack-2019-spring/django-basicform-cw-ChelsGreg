from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Account


# Create your views here.
def index(request):
    allAccount = Account.objects.all()

    context = {
        "allAccounts": allAccount
    }
    return render(request, 'accountApp/index.html', context)


def printAccount(request):
    print( request.POST)

    return HttpResponse("Welcome to " + request.POST['printAccount'] + "s Account")


def addFive(request, accountID):
    thisAccount = get_object_or_404(Account, pk=accountID)
    thisAccount.checking += 5
    thisAccount.save()
    return redirect("index")

