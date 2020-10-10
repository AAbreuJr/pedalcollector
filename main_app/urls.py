from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pedalboards/', views.pedalboards_index, name='index'),
  path('pedalboards/<int:pedalboard_id>/', views.pedalboards_detail, name='detail'),
  path('pedalboards/create/', views.PedalboardCreate.as_view(), name='pedalboards_create'),
  path('pedalboards/<int:pk>/update/', views.PedalboardUpdate.as_view(), name='pedalboards_update'),
  path('pedalboards/<int:pk>/delete/', views.PedalboardDelete.as_view(), name='pedalboards_delete'),
  # associate a pedal with a board (M:M)
  path('pedalboards/<int:pedalboard_id>/assoc_pedal/<int:pedal_id>/', views.assoc_pedal, name='assoc_pedal'),
  # unassociate a pedal with a board
  path('pedalboards/<int:pedalboard_id>/unassoc_pedal/<int:pedal_id>/', views.unassoc_pedal, name='unassoc_pedal'),
  path('pedals/', views.PedalList.as_view(), name='pedals_index'),
  path('pedals/<int:pk>/', views.PedalDetail.as_view(), name='pedals_detail'),
  path('pedals/create/', views.PedalCreate.as_view(), name='pedals_create'),
  path('pedals/<int:pk>/update/', views.PedalUpdate.as_view(), name='pedals_update'),
  path('pedals/<int:pk>/delete/', views.PedalDelete.as_view(), name='pedals_delete'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
]