from django.shortcuts import render
from .models import Frog

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def frog_index(request):
  frogs = Frog.objects.all()
  return render(request, 'frogs/index.html', { 'frogs': frogs })

def frog_detail(request, frog_id):
  frog = Frog.objects.get(id=frog_id)
  return render(request, 'frogs/detail.html', { 'frog': frog})