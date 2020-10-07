from django.db import models

# Create your models here.
class Pedal(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    type = models.CharField(max_length=250)
    stereo = models.CharField(max_length=100)

    def __str__(self):
        return self.name
