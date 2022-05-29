from pyexpat import model
from venv import create
from wsgiref.simple_server import demo_app
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class StreamingPlaform(models.Model):
    name  = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    website= models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(max_length=50)
    platform = models.ForeignKey(StreamingPlaform, on_delete=models.CASCADE,related_name="movies")
    story_line  = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators= [MinValueValidator(1),MaxValueValidator(5)])
    discription = models.CharField(max_length=50)
    movies = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='review')
    active = models.BooleanField(default=True)
    created_at =models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + " | " + self.movies.title