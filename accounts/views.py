from django.shortcuts import render

def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')

def services(request):
    return render(request, 'accounts/services.html')