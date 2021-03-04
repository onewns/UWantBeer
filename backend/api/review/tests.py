from django.test import TestCase
from .models import ReviewModel
from .serializers import ReviewSerializer
from django.conf import settings
from . import views

# Create your tests here.
class ModelTest(TestCase):
    def modelCreationTest(self):
        model = ReviewModel(
            title = "test",
            content = "test",
            author = settings.AUTH_USER_MODEL
        )
        return model

    def serializerTest(self):
        serializer = ReviewSerializer(modelCreationTest())
        return serializer

    