from django.shortcuts import render

from .models import Project

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
def home(request):
    return render(request,"main/home.html")
def about(request):
    return render(request,"main/about.html")


def projects(request):
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects": projects})

def skills(request):
    return render(request,"main/skills.html")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Sending email
        send_mail(
            f"New Message from {name}",
            f"Message: {message}\n\nFrom: {name} ({email})",
            settings.DEFAULT_FROM_EMAIL,  
            ['venusaaripalli69@gmail.com'],  # Email to send to
        )
        return HttpResponse("Message sent successfully!")
    return render(request, 'contact.html')
