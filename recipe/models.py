from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


"""
Author model:
    Name (CharField)
    Bio (TextField)

Recipe Model:
    Title (CharField)
    Author (link, ForeignKey)
    Description (TextField)
    Time Required (Charfield) (for example, "One hour")
    Instructions (TextField)
"""


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # One-to-one relationship between author and user

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
