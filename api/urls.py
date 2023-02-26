from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="songs"),
    path('songs/', views.get_songs, name="songs"),
    
    path('songs/add/', views.add_song, name="add-song"),
    
    path('songs/<str:pk>/update/', views.update_song, name="update-song"),
    
    path('songs/<str:pk>/', views.get_song, name="song"),
        
    path('songs/<str:pk>/delete/', views.delete_song, name="delete-song"),
]
