from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Frog, LilyPad
from .forms import FeedingForm
from django.contrib.auth.views import LoginView

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def frog_index(request):
  frogs = Frog.objects.filter(user=request.user)
  return render(request, 'frogs/index.html', { 'frogs': frogs })

@login_required
def frog_detail(request, frog_id):
  frog = Frog.objects.get(id=frog_id)
  lilypads_frog_doesnt_have = LilyPad.objects.exclude(id__in = frog.lilypads.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'frogs/detail.html', { 'frog': frog, 'feeding_form': feeding_form, 'lilypads': lilypads_frog_doesnt_have})

@login_required
def add_feeding(request, frog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.frog_id = frog_id
    new_feeding.save()
  return redirect('frog-detail', frog_id=frog_id)

@login_required
def assoc_lilypad(request, frog_id, lilypad_id):
  Frog.objects.get(id=frog_id).lilypads.add(lilypad_id)
  return redirect('frog-detail', frog_id=frog_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('frog-index')
    else:
      error_message ='Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class FrogCreate(LoginRequiredMixin, CreateView):
  model = Frog
  fields = ['name', 'species', 'description', 'age']
  
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class FrogUpdate(LoginRequiredMixin, UpdateView):
  model = Frog
  fields = ['species', 'description', 'age']

class FrogDelete(LoginRequiredMixin, DeleteView):
  model = Frog
  success_url = '/frogs/'

class LilyPadCreate(LoginRequiredMixin, CreateView):
  model = LilyPad
  fields = '__all__'

class LilyPadList(LoginRequiredMixin, ListView):
  model = LilyPad

class LilyPadDetail(LoginRequiredMixin,DetailView):
  model = LilyPad

class LilyPadUpdate(LoginRequiredMixin, UpdateView):
  model = LilyPad
  fields = ['name', 'color']

class LilyPadDelete(LoginRequiredMixin, DeleteView):
  model = LilyPad
  success_url = '/lilypads/'

class Home(LoginView):
  template_name = 'home.html'