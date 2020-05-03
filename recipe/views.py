from django.shortcuts import render

from recipe.models import Author, RecipeItem


def index(request):
    author = Author.objects.all()
    recipe = RecipeItem.objects.all()
    return render(request, 'index.html', {"author_data": author, "recipe_data": recipe})


def recipe_details(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, "recipe_details.html", {"recipe": recipe})


def author_details(request, id):
    author = Author.objects.get(id=id)
    recipe_data = RecipeItem.objects.all()
    return render(request, "author_details.html", {"author": author, "recipe_data": recipe_data})

