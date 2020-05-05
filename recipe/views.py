from django.shortcuts import render, reverse, HttpResponseRedirect

from recipe.models import Author, RecipeItem
from recipe.forms import RecipeAddForm, AuthorAddForm


def index(request):
    author = Author.objects.all()
    recipe = RecipeItem.objects.all()
    return render(request, 'index.html', {"author_data": author, "recipe_data": recipe})

# RECIPES

def recipe_details(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, "recipe_details.html", {"recipe": recipe})


def recipe_add_views(request):
    html = "recipe_form.html"

    # POST request
    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid(): # MUST DO before every POST request
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                description=data['description'],
                instructions=data['instructions'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse("homepage"))


    # GET request
    form = RecipeAddForm()

    return render(request, html, {'form': form})


# AUTHORS

def author_details(request, id):
    author = Author.objects.get(id=id)
    recipe_data = RecipeItem.objects.all()
    return render(request, "author_details.html", {"author": author, "recipe_data": recipe_data})


def author_add_views(request):
    html = "author_form.html"
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()

    form = AuthorAddForm()

    return render(request, html, {'form': form})
