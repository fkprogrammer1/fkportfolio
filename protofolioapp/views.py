from django.shortcuts import render
from . models import Project
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
def home(request):
  
    project=Project.objects.all()[0:3]

    
    return render(request,"base.html",{"project":project})

def all(request):
    project=Project.objects.all()
    return render(request,'project.html',{"project":project})
def singleblog(request,slug):
    post=Project.objects.get(slug=slug)
    return render(request,"blog.html",{"blog":post})