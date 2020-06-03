from django.shortcuts import render, reverse, HttpResponseRedirect
from recipe.models import Author, RecipeItem
from recipe.forms import RecipeAddForm, AuthorAddForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def index(request):
    author = Author.objects.all()
    recipe = RecipeItem.objects.all()
    return render(request, 'index.html', {"author_data": author, "recipe_data": recipe})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'author_form.html', {'form': form})


@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


# RECIPES

@login_required
def recipe_edit(request, id):
    recipe = RecipeItem.objects.get(id=id)
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if request.user.author == recipe.author or request.user.is_staff:
            if form.is_valid():
                data = form.cleaned_data
                recipe.title = data['title']
                recipe.author = data['author']
                recipe.description = data['description']
                recipe.instructions = data['instructions']
                recipe.save()
            return HttpResponseRedirect(reverse('recipe_details', args=(id,)))
    form = RecipeAddForm(initial = {
        'title': recipe.title, 
        'author': recipe.author,
        'description': recipe.description,
        'instructions': recipe.instructions, 
    })
    return render(request, 'recipe_form.html', {'form': form})


@login_required
def favorite_add(request, id):
    current_user = request.user.author
    favorite_recipe = RecipeItem.objects.get(id=id)
    current_user.favorite.add(favorite_recipe)
    current_user.save()
    return HttpResponseRedirect(reverse('recipe_details', args={id,})) 

@login_required
def favorite_remove(request, id):
    current_user = request.user.author
    favorite_recipe = RecipeItem.objects.get(id=id)
    current_user.favorite.remove(favorite_recipe)
    current_user.save()
    return HttpResponseRedirect(reverse('recipe_details', args={id,}))


def recipe_details(request, id):
    recipe = RecipeItem.objects.get(id=id)
    if request.user.is_authenticated:
        current_author = request.user.author.favorite.all()
        return render(request, "recipe_details.html", {"recipe": recipe, "current_author": current_author})
    return render(request, "recipe_details.html", {"recipe": recipe})


@login_required
def recipe_add_views(request):
    html = "recipe_form.html"
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
    form = RecipeAddForm()
    return render(request, html, {'form': form})


# AUTHORS

def author_details(request, id):
    author = Author.objects.get(id=id)
    recipe_data = RecipeItem.objects.all()
    return render(request, "author_details.html", {"author": author, "recipe_data": recipe_data})


def author_add_views(request):
    form = AuthorAddForm()
    html = "author_form.html"
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                )
            new_user.save()
            new_author = Author(
                name=data['name'],
                bio=data['bio'],
                user=new_user,
            )
            new_author.save()
            return render(request, 'index.html', {'data': data, 'new_author': new_author})    
    return render(request, html, {'form': form})


