from django.urls import path

from . import views
app_name = 'music'
urlpatterns = [
    path('', views.index, name='index'),

  # ex: /polls/5/
    path('<int:album_id>/', views.detail, name='detail'),

    # ex: /polls/5/favorite
    path('<int:album_id>/favorite/', views.favorite, name='favorite'),
]
