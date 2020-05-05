from django.urls import path

from recipe import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipes/<int:id>/', views.recipe_details, name="recipe_details"),
    path('authors/<int:id>/', views.author_details, name="author_details"),
    path('recipeadd/', views.recipe_add_views, name="recipe_add_view"),
    path('authoradd/', views.author_add_views, name="author_add_view")
    # path('admin/', admin.site.urls),
]
