from django.urls import path
from . import views

urlpatterns = [
    path('svd/', views.svd), #SVD algorithm 
]