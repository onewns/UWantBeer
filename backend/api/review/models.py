from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from beer.models import Beer

User = get_user_model()

# Create your models here.
class ReviewModel(models.Model):
    
    #title
    # title = models.CharField(max_length=100)

    #rate
    rate = models.IntegerField(default=5)

    #content
    content = models.CharField(max_length=500, null=True)
    
    #beer
    beer = models.ForeignKey(Beer, related_name='reviews', on_delete=models.CASCADE, null=True)

    #beer name
    beer_name = models.CharField(max_length=500, null=True)

    #author
    author = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE, null=True)

    #author name
    author_name = models.CharField(max_length=500, null=True)

    #image
    image_url = models.URLField(max_length=200, null=True)
    
    #created date
    created_date = models.DateField(auto_now_add=True, null=True)
    
    #edited date
    last_edit_date = models.DateField(auto_now=True, null=True)

    #toString method
    # def __str__(self):
    #     result = {
    #         # "title": self.title,
    #         "rate": self.rate,
    #         "content": self.content,
    #         "author": self.author,
    #         "created_date": self.created_date,
    #         "last_edit_date": self.last_edit_date,
    #     }
    #     return result
