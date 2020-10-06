from django.shortcuts import render
from django.http import HttpResponse

class Pedal:
    def __init__ (self, name, company, type, stereo):
        self.name = name
        self.company = company
        self.type = type
        self.stereo = stereo

pedals = [
    Pedal('Bloom', 'Jackson Audio', 'Compressor', 'no'),
    Pedal('POG 2', 'Electro Harmonix', 'Octave', 'no'),
    Pedal('Superbolt', 'JHS Audio',  'Overdrive', 'no')
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>We Love Pedals</h1>')

def about(request):
    return render(request, 'about.html')

def pedals_index(request):
    return render(request, 'pedals/index.html', { 'pedals': pedals })