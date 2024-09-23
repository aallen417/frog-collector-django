from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('frogs/', views.frog_index, name='frog-index'),
  path('frogs/<int:frog_id>/', views.frog_detail, name='frog-detail'),
  path('frogs/create/', views.FrogCreate.as_view(), name='frog-create'),
  path('frogs/<int:pk>/update', views.FrogUpdate.as_view(), name='frog-update'),
  path('frogs/<int:pk>/delete', views.FrogDelete.as_view(), name='frog-delete'),
  path('frogs/<int:frog_id>/add-feeding', views.add_feeding, name='add-feeding'),
  path('lilypads/create/', views.LilyPadCreate.as_view(), name='lilypad-create'),
  path('lilypads/<int:pk>/', views.LilyPadDetail.as_view(), name='lilypad-detail'),
  path('lilypads/', views.LilyPadList.as_view(), name='lilypad-index'),
  path('lilypads/<int:pk>/update/', views.LilyPadUpdate.as_view(), name='lilypad-update'),
  path('lilypads/<int:pk>/delete/', views.LilyPadDelete.as_view(), name='lilypad-delete'),
]