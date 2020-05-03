from django.db import models


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

    def __str__(self):
        return self.name



class RecipeItem(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.CharField(max_length=30)
    instructions = models.TextField()

    def __str__(self):
        return self.title
