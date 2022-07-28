from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    name="prashant"
    return render(request,'solution/home.html',{'name':name})