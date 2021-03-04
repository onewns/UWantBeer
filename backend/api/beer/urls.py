from django.urls import path, re_path
from . import views

urlpatterns = [
    path('all/', views.getAllBeer), #Get all beers
    path('<int:beer_id>/', views.getSingleBeer), #Get single beer information
    path('new/', views.addNewBeer), #Add New Beer
    path('edit/<int:beer_id>/', views.editBeerInfo), #Edit Beer Information
    path('delete/<int:beer_id>/', views.deleteBeer), #Delete Beer
    path('recommendation/', views.recommendation), #Delete Beer
    re_path(r'^search$', views.searchBeer), #Search Beer
    # path('csv/', views.saveCSV), #OneTimeCSV 
]

