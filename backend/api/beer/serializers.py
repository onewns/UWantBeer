from rest_framework import serializers
from .models import Beer

class BeerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Beer
        fields = ["id", "name", "name_kr", "brew_name", "style", "country", "abv", "image_url"]