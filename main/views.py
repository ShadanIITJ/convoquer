from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import circket
from django.contrib.auth.models import User
# Create your views here.

def base(request):
    return render(request,'main/main.html')


def team(request):
    return render(request,'main/team.html')

def gallery(request):
    return render(request,'main/gallery.html')

def broucher(request):
    return render(request,'main/brouser.html')

def rule(request):
    return render(request,'main/rulebook.html')

def event(request):
    return render(request,'main/events.html')
def sponser(request):
    return render(request,'main/sponsers.html')

def circket(request):
    result = circket.objects.all()
    return render(request,'main/circket_result.html')