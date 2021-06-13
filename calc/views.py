from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Home.html',{'Name':'Friend Function'})

def Login(request):

     UserName = request.GET['UserName']
     Password = request.GET['Password']
     # if  str(var1)=='None':
     #      res = 'UserName is Empty '
     # else:
     #     res = 'UserName is not Empty '+var1

     return render(request,"Login.html",{'Result':UserName})