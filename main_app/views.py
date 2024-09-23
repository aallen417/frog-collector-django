from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Frog
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'frogs/detail.html', { 'frog': frog, 'feeding_form': feeding_form})

def add_feeding(request, frog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.frog_id = frog_id
    new_feeding.save()
  return redirect('frog-detail', frog_id=frog_id)

class FrogCreate(CreateView):
  model = Frog
  fields = '__all__'
  success_url = '/frogs/'

class FrogUpdate(UpdateView):
  model = Frog
  fields = ['species', 'description', 'age']

class FrogDelete(DeleteView):
  model = Frog
  success_url = '/frogs/'