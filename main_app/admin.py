from django.contrib import admin
from .models import Pedalboard, Pedal, Photo

# Register your models here.
admin.site.register(Pedalboard)
admin.site.register(Pedal)
admin.site.register(Photo)