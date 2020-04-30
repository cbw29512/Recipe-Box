from django.shortcuts import render

from recipe.models import RecipeItem


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})

# def recipe(request):
#     data = RecipeItem.objects.all()
#     return render(request, 'index.html', {'data': data})
