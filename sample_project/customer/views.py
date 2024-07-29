from django.shortcuts import render
from customer.models import User

# Create your views here.
def registration(request):
    if request.method=="POST":
        obj=User()
        obj.name=request.POST.get('custname')
        obj.address=request.POST.get('address')
        obj.gender=request.POST.get('gen')
        obj.email=request.POST.get('email')
        obj.phone_no=request.POST.get('ph_no')
        obj.save()
    return render(request, 'customer/user_reg.html')

def view(request) :
    oblist=User.objects.all()
    context={
        'objval':oblist,
    }

    return render(request, 'customer/view.html',context)
