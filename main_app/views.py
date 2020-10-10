from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Pedalboard, Pedal

# S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
# BUCKET = 'pedalboardcollector'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PedalboardCreate(LoginRequiredMixin, CreateView):
  model = Pedalboard
  fields = ['name', 'company', 'size', 'color']

  def form_valid(self, form):
    # Assign the logged in user
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class PedalboardUpdate(LoginRequiredMixin, UpdateView):
  model = Pedalboard
  fields = ['name', 'company', 'size', 'color']

class PedalboardDelete(LoginRequiredMixin, DeleteView):
  model = Pedalboard
  success_url = '/pedalboards/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def pedalboards_index(request):
  pedalboards = Pedalboard.objects.filter(user = request.user)
  # cats = request.user.cat_set.all()
  return render(request, 'pedalboards/index.html', { 'pedalboards': pedalboards })

@login_required
def pedalboards_detail(request, pedalboard_id):
  pedalboard = Pedalboard.objects.get(id=pedalboard_id)
  # Get the toys the cat doesn't have
  pedals_pedalboard_doesnt_have = Pedal.objects.exclude(id__in = pedalboard.pedals.all().values_list('id'))
  # Instantiate FeedingForm to be rendered in the template
  return render(request, 'pedalboards/detail.html', {
    'pedalboard':pedalboard,
    # Add the toys to be displayed
    'pedals': pedals_pedalboard_doesnt_have
  })

# @login_required
# def add_photo(request, pedalboard_id):
# 	# photo-file was the "name" attribute on the <input type="file">
#   photo_file = request.FILES.get('photo-file', None)
#   if photo_file:
#     s3 = boto3.client('s3')
#     # need a unique "key" for S3 / needs image file extension too
#     key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#     # just in case something goes wrong
#     try:
#       s3.upload_fileobj(photo_file, BUCKET, key)
#       # build the full url string
#       url = f"{S3_BASE_URL}{BUCKET}/{key}"
#       # we can assign to cat_id or cat (if you have a cat object)
#       photo = Photo(url=url, pedalboard_id=pedalboard_id)
#       photo.save()
#     except:
#       print('An error occurred uploading file to S3')
#   return redirect('detail', pedalboard_id=pedalboard_id)

@login_required
def assoc_pedal(request, pedalboard_id, pedal_id):
  Pedalboard.objects.get(id=pedalboard_id).pedals.add(pedal_id)
  return redirect('detail', pedalboard_id=pedalboard_id)

@login_required
def unassoc_pedal(request, pedalboard_id, pedal_id):
  Pedalboard.objects.get(id=pedalboard_id).pedals.remove(pedal_id)
  return redirect('detail', pedalboard_id=pedalboard_id)

class PedalList(LoginRequiredMixin, ListView):
  model = Pedal

class PedalDetail(LoginRequiredMixin, DetailView):
  model = Pedal

class PedalCreate(LoginRequiredMixin, CreateView):
  model = Pedal
  fields = '__all__'

class PedalUpdate(LoginRequiredMixin, UpdateView):
  model = Pedal
  fields = ['name', 'company', 'color']

class PedalDelete(LoginRequiredMixin, DeleteView):
  model = Pedal
  success_url = '/pedals/'