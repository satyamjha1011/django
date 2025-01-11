from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello, World!")
    return render(request,'website/index.html')

def about(request):
   # return HttpResponse("Hello, World! This is a great website and will be available at about pages")
    return render(request,'website/about.html')
def contact(request):
    #return HttpResponse("Hello, World! And this is our contact page on  our website")
    return render(request,'website/contact.html')

    
