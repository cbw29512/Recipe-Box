from django.urls import path
from recipe import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipes/<int:id>/', views.recipe_details, name="recipe_details"),
    path('authors/<int:id>/', views.author_details, name="author_details"),
    path('recipeadd/', views.recipe_add_views, name="recipe_add_view"),
    path('authoradd/', views.author_add_views, name="author_add_view"),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('recipe_edit/<int:id>', views.recipe_edit, name='recipe_edit'),
    path('favorite_add/<int:id>', views.favorite_add, name='favorite_add'),
    path('favorite_remove/<int:id>', views.favorite_remove, name='favorite_remove'),
    # path('admin/', admin.site.urls),
]
