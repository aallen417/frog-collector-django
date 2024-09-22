from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('frogs/', views.frog_index, name='frog-index'),
  path('frogs/<int:frog_id>/', views.frog_detail, name='frog-detail'),
  path('frogs/create/', views.FrogCreate.as_view(), name='frog-create'),
]