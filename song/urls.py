from django.urls import path
from . import views


urlpatterns = [
    path('song/', views.songs, name="song"),
    path('add-song/', views.add_song, name="add-song"),
    path('update-song/<str:pk>/', views.update_song, name="update-song"),
    path('delete/<str:pk>/', views.delete_song, name="delete"),
]
