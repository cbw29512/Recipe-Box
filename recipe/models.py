from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50, default=None)
    bio = models.TextField()
    favorite = models.ManyToManyField(
        'RecipeItem', 
        related_name='favorite', 
        default = None, 
        blank=True, 
        symmetrical=False
        )
    
    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    time = models.CharField(max_length=30)
    instructions = models.TextField()
    

    def __str__(self):
        return self.title


