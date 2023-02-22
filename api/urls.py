from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes), 
    path('songs/', views.get_songs), 
    path('songs/add/', views.add_song),
    path('songs/<str:pk>/update', views.update_song),
    path('songs/<str:pk>/delete', views.delete_song), 
]
