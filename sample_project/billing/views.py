from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msg(request):
    return HttpResponse("Message")



def add_num(request):
    if request.method == "POST":
        n1=request.POST.get("bno")
        n2=request.POST.get("pdate")
        s=int(n1) + int(n2)
        context={
            'sum':s
        }
        return render(request,'billing/add_num.html',context)
    return render(request,'billing/add_num.html')

