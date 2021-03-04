from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import ReviewModel
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from beer.models import Beer
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
@api_view(['GET'])
def getAllReview(request):
    reviews = ReviewModel.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def getReview(request, review_id):
    review = get_object_or_404(ReviewModel, pk=review_id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def getReviewByBeer(request, beer_id):
    reviews = ReviewModel.objects.all().filter(beer=beer_id)
    for i in reviews:
        print(i.author.username)
        i.author_name = i.author.username
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def getReviewByAuthor(request, user_id):
    reviews = ReviewModel.objects.all().filter(author=user_id)
    for i in reviews:
        if i.beer.name_kr:
            i.beer_name = i.beer.name_kr
        else:
            i.beer_name = i.beer.name
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=200)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createReview(request, beer_id):
    serializer = ReviewSerializer(data=request.data)
    beer = get_object_or_404(Beer, pk=beer_id)
    if serializer.is_valid():
        serializer.save(author=request.user, beer=beer)
        return Response(serializer.data, status=200)
        
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def editReview(request, review_id):
    review = get_object_or_404(ReviewModel, pk=review_id)
    if review.author != request.user:
        return Response({"message":"작성자만 글을 수정할 수 있습니다"})

    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
    return Response(serializer.errors)


@api_view(["DELETE"])
def deleteReview(request, review_id):
    review = get_object_or_404(ReviewModel, pk=review_id)
    if review.author == request.user:
        review.delete()
        return Response(
            {
                "status":"success",
                "message":"리뷰가 성공적으로 삭제되었습니다."
            })

    else:
        return Response({
            "status":"failed",
            "message":"리뷰 작성자만 삭제가 가능합니다."
        })
    
