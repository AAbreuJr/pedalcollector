from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Pedal(models.Model):
  name = models.CharField(max_length=50)
  company = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pedals_detail', kwargs={'pk': self.id})

class Pedalboard(models.Model):
  name = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  size = models.CharField(max_length=10)
  color = models.CharField(max_length=10)
  pedals = models.ManyToManyField(Pedal)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'pedalboard_id': self.id})


class Photo(models.Model):
  url = models.CharField(max_length=200)
  pedalboard = models.ForeignKey(Pedalboard, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for pedalboard_id: {self.pedalboard_id} @{self.url}"