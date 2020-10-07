from django.shortcuts import render
from .models import Pedal



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pedals_index(request):
    pedals = Pedal.objects.all()
    return render(request, 'pedals/index.html', { 'pedals': pedals}) #how we will pass data into it

def pedals_detail(request, pedal_id):
    pedal = Pedal.objects.get(id=pedal_id)
    return render(request, 'pedals/detail.html', { 'pedal': pedal })