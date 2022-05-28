
from django.urls import path
from app1 import views
urlpatterns = [
    
    path('',views.Movie_list.as_view(), name='Movies'),
    path('details/<int:pk>',views.MovieDetails.as_view(), name='Movies'),
]
