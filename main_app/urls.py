from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # this is the home route, the same as '/'. the name arg is a keyword arg that we can use to refer to this path in other parts of our code
    path('about/', views.about, name='about'), # this is the about route, the same as '/about/'
    path('cats/', views.cats_index, name='index'),
]