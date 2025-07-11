from django.shortcuts import render, redirect
from django.contrib import messages
from tracker.models import *
from django.db.models import Sum
 


def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        
        if not description:
            messages.info(request, "Description cannot be blank") 
            return redirect('index')
        
        try :
            amount = float(amount)
        except Exception as e:

            messages.info(request, "Should be a Number")
            return redirect('index')
        
        Transaction.objects.create(
            description = description,
            amount = amount

        )
        messages.info(request, "transaction added successfully!")
        return redirect('index')
    context = {'transactions': Transaction.objects.all(),
               'balance': Transaction.objects.all().aggregate(balance= Sum('amount'))['balance'] or 0,
               'income': Transaction.objects.filter(amount__gte = 0).aggregate(income = Sum('amount'))['income'] or 0,
               'expense': Transaction.objects.filter(amount__lte = 0).aggregate(expense = Sum('amount'))['expense'] or 0,
                 }
 

        
      
    return render (request, "index.html", context)

def deleteTransaction(request, id):
    Transaction.objects.get(id = id).delete()
    return redirect('index')

# Create your views here.
 