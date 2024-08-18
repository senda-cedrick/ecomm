from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Item,Order,OrderItem

class HomeView(ListView):
    model = Item 
    template_name='index.html'
def home(request):
    return render(request,'index.html')
def products(request):
    return render(request,'products.html')
def singleproduct(request):
    return render(request,'singleproduct.html')
def store(request):
    return render(request,'store.html')