from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Item


def home(request):
  items = Item.objects.all()
  return render(request, 'home.html', { 'items': items })  

def items_index(request):
  items = Item.objects.all()
  return render(request, 'items/index.html', { 'items': items })  

class ItemCreate(CreateView):
  model = Item
  fields = ['description']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/'
