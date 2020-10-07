from django.db import models
from django.urls import reverse

# Create your models here.
class Pedalboard(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pedalboard_id': self.id})
