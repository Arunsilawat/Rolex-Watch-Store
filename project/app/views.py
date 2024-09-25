from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def watch(request):
    return render(request,'watch.html')
def about(request):
    return render(request,'about.html')
def new(request):
    return render(request,'new.html')
def service(request):
    return render(request,'service.html')
def sports(request):
    return render(request,'sports.html')