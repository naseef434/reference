from django.db import models

# Create your models here.


class StreamingPlaform(models.Model):
    name  = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    website= models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(max_length=50)
    platform = models.ForeignKey(StreamingPlaform, on_delete=models.CASCADE,related_name="watchLsit")
    story_line  = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title