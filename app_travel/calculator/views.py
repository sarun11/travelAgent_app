from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request, 'index.html', {'name': 'Sarun'})

def add(request):
    
    
    n1= request.POST['num1']
    n2= request.POST['num2']
    
    ans= int(n1)+ int(n2)
    
    return render (request, 'answer.html', {'answer': ans})