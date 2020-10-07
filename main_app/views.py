from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pedalboard



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pedalboards_index(request):
    pedalboards = Pedalboard.objects.all()
    return render(request, 'pedalboards/index.html', { 'pedalboards': pedalboards}) #how we will pass data into it

def pedalboards_detail(request, pedalboard_id):
    pedalboard = Pedalboard.objects.get(id=pedalboard_id)
    return render(request, 'pedalboards/detail.html', { 'pedalboard': pedalboard })

class PedalboardCreate(CreateView):
    model = Pedalboard
    fields = '__all__'

class PedalboardUpdate(UpdateView):
    model = Pedalboard
    fields = '__all__'

class PedalboardDelete(DeleteView):
    model = Pedalboard
    success_url = '/pedalboards/'
