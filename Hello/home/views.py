from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.http import JsonResponse



# Create your views here.
def index(request):
    context = {
        'variable1':'this is a variable which has been sent',
        'variable2':'55555'
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is homepage") 
def services(request):
    return render (request,'services.html')
    # return HttpResponse("This is about services page")
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        concern=request.POST.get('concern')
        contact = Contact(name=name,email=email,phone=phone,concern=concern,date=datetime.today())
        contact.save()
        messages.success(request, 'Your request has been sent!')
    return render (request,'contact.html')
    # return HttpResponse("This is about contacts page")
def about(request):
    return render (request,'about.html')

def updateItem(request):
    return JsonResponse("Item was added",safe = False)