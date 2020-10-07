from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pedalboards/', views.pedalboards_index, name='index'),
    path('pedalboards/<int:pedalboard_id>', views.pedalboards_detail, name='detail'),
    path('pedalboards/create/', views.PedalboardCreate.as_view(), name='pedalboards_create'),
    path('pedalboards/<int:pk>/update/', views.PedalboardUpdate.as_view(), name='pedalboards_update'),
    path('pedalboards/<int:pk>/delete/', views.PedalboardDelete.as_view(), name='pedalboards_delete'),
]