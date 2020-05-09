from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipe.models import Author, RecipeItem
from recipe.forms import RecipeAddForm, AuthorAddForm, LoginForm


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
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'author_form.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


# RECIPES

def recipe_details(request, id):
    recipe = RecipeItem.objects.get(id=id)
    return render(request, "recipe_details.html", {"recipe": recipe})


@login_required
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


@login_required
def author_add_views(request):
    if request.user.is_staff:
        html = "author_form.html"
        if request.method == "POST":
            form = AuthorAddForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(
                    username=data['username'],
                    password=data['password']
                )
                Author.objects.create(
                    name=data['name'],
                    bio=data['bio'],
                    user=new_user
                )
                return HttpResponseRedirect(reverse('homepage'))

        form = AuthorAddForm()

        return render(request, html, {'form': form})
    return HttpResponseRedirect(reverse('homepage'))
