from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Ejemplo(request):
    return render(request,"home.html")


def Ejemplo2(request):
     return render(request, 'nuevo.html')



