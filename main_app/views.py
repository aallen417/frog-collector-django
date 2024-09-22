from django.shortcuts import render

# Create your views here.

class Frog:
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

frogs = [
  Frog('Croaker', 'American Bullfrog', 'Loud', 6),
  Frog('Hippity', 'Northern Leopard Frog', 'Loves to jump', 3),
  Frog('Hop', 'Glass Frog', 'Hops between lily pads', 4),
  Frog('Skrem', 'American Bullfrog', 'Louder', 0),
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def frog_index(request):
  return render(request, 'frogs/index.html', { 'frogs': frogs })