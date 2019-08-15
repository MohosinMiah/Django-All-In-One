from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('favorite', views.favorite, name='favorite'),
  # ex: /polls/5/
    path('<int:album_id>/', views.detail, name='detail'),
]
