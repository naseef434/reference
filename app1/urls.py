
from django.urls import path
from app1 import views
urlpatterns = [
    
    path('streaming/',views.StreamingPlatfromList.as_view(),name="Streaming-List"),
    path('movies/',views.Movie_list.as_view(), name='Moviesss'),
    path('movies/<int:pk>',views.MovieDetails.as_view(), name='Movies'),
    
    path('review/',views.ReviewListAll.as_view(),name="Review-List-All"),
    # path('review/<int:pk>/',views.ReviewDetails.as_view(),name="Review-single-details")
    path('stream/<int:pk>/create_review', views.CreateReview.as_view(),name="create-review-"),
    path('stream/<int:pk>/review', views.ReviewList.as_view(),name="Review-List"),
    path('stream/review/<int:pk>', views.ReviewDetails.as_view(),name="Review-List")
    
]
