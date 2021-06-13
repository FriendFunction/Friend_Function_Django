from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Home.html',{'Name':'Friend Function'})

def Login(request):

     val1 = request.POST.get('UserName')
     val2 = request.POST.get('Password')

     res = 2 + 5
     return render(request,"Login.html",{'Result':res});