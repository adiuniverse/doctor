from django.shortcuts import render

# Create your views here.
def google_master(request):
    return render(request,'client/master.html')
def google_home(request):
    return render(request,'client/home.html')
def google_about(request):
    return render(request,'client/about.html')
def google_contact(request):
    return render(request,'client/contact.html')





















