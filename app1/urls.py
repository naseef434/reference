
from django.urls import path
from app1 import views
urlpatterns = [
    
    path('streaming/',views.StreamingPlatfromList.as_view(),name="Streaming-List"),
    path('movies/',views.Movie_list.as_view(), name='Moviesss'),
    path('movies/<int:pk>',views.MovieDetails.as_view(), name='Movies'),
    
    path('review/',views.ReviewList.as_view(),name="Review-List"),
    path('review/<int:pk>/',views.ReviewDetails.as_view(),name="Review-single-details")
    
]
