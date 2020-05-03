from django.urls import path

from recipe import views


urlpatterns = [
    path('', views.index),
    path('recipes/<int:id>/', views.recipe_details, name="recipe_details"),
    path('authors/<int:id>/', views.author_details, name="author_details")
    # path('admin/', admin.site.urls),
]
