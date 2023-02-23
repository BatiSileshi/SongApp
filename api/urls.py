from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="songs"),
    path('songs/', views.get_songs, name="songs"),
    path('songs/<str:pk>/', views.get_song, name="song"),
    path('add-song/', views.add_song, name="add-song"),
    path('update-song/<str:pk>/', views.update_song, name="update-song"),
    path('delete/<str:pk>/', views.delete_song, name="delete"),
]
