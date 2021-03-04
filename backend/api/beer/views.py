from django.shortcuts import render, get_object_or_404
from django.db.models import F, Func, Value, Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Beer
import csv
import pandas as pd
import random
from .serializers import BeerSerializer

from .firebase import getURL
# Create your views here.

#Return all beers
@api_view(['GET'])
def getAllBeer(request):
    beers = Beer.objects.all()
    #데이터 전부다 들어오면 해제
    count = 0
    for beer in beers:
        count += 1
        print("assigning....", count)
        beer.image_url = getURL(beer.image_file_name)

    print("assign Done")
    serializer = BeerSerializer(beers, many=True)
    return Response(serializer.data)


#Get specified beer information
@api_view(['GET'])
def getSingleBeer(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    beer.image_url = getURL(beer.image_file_name)
    serializer = BeerSerializer(beer)
    return Response(serializer.data)


#API to add new beer
@api_view(['POST'])
def addNewBeer(request):
    beer_serializer = BeerSerializer(data=request.data)
    if beer_serializer.is_valid():
        beer_serializer.save()
        return Response(request.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


#API to edit beer information
@api_view(['PUT'])
def editBeerInfo(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    serializer = BeerSerializer(beer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
    # return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.error)


#API to delete specified beer
@api_view(['DELETE'])
def deleteBeer(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id) #Return 404 if beer doesn't exist
    beer.delete()
    return Response(status.HTTP_200_OK)
    

#API to search beers
@api_view(['GET'])
def searchBeer(request):
    #Get keyword from query string
    keyword = request.GET.get('keyword')
    style = request.GET.get('style')
    country = request.GET.get('country')
    abvmax = request.GET.get('abvmax')
    abvmin = request.GET.get('abvmin')
    limit = int(request.GET.get('limit'))
    #Get all beer
    beer = Beer.objects.all()
    #Create nospace column and add beer name after removing all spaces
    if keyword:
        keyword = keyword.replace(" ", "")
        preprocess = beer.annotate(
            nospace1=Func( F('name_kr'), Value(" "), Value(""), function="replace" ), 
            nospace2=Func( F('name'), Value(" "), Value(""), function="replace"),
            lowercase=Func( F('name'), function="lower")
            )
    #Search beer for keyword, country, style, abv range
        rst = preprocess.filter((Q(nospace1__contains=keyword) | Q(nospace2__contains=keyword) | Q(lowercase__contains=keyword))&Q(abv__gte=abvmin)&Q(abv__lte=abvmax))
    else:
        rst = beer.filter(Q(abv__gte=abvmin)&Q(abv__lte=abvmax))
    if style == 'Etc':
        rst = rst.exclude(Q(style='Lager') | Q(style='Ale'))
    elif style != 'All':
        rst = rst.filter(style=style)
    
    if country == 'Etc':
        rst = rst.exclude(country = 'KR')
    elif country != 'All':
        rst = rst.filter(country = country)
    
    end = False

    if len(rst) <= 12 and len(rst):
        end = True
    elif len(rst) >= limit:
        rst = rst[limit-12:limit]
    else:
        rst = rst[limit-12:]
        end = True

    for beer in rst:
        beer.image_url = getURL(beer.image_file_name)

    serializer = BeerSerializer(rst, many=True)
    if serializer.data and not end:
        return Response(serializer.data)
    elif serializer.data:
        return Response(serializer.data, status=202)
    else:
        return Response(status=204)
    
    return Response(status=400)

#Onetime API to save CSV(Finished)
@api_view(['GET'])
def saveCSV(request):
    with open('beer/csv/beer.csv', mode='r', encoding='cp949') as beer_list:
        dictionary = csv.DictReader(beer_list)
        beer_df = pd.DataFrame(dictionary)

        beers = []
        for i in range(len(beer_df)):
            beer = (beer_df['name'][i], 
            beer_df['name_kr'][i],
            beer_df['bre_name'][i],
            beer_df['country'][i],
            beer_df['category'][i],
            beer_df['style'][i],
            beer_df['abv'][i],
            beer_df['image'][i])
            
            beers.append(beer)

        # ADD TO DATABASE
        beer_set = Beer.objects.all()
        for beer in beers:
            if not beer_set.filter(name=beer[0]).exists():
                Beer.objects.create(
                    name=beer[0],
                    name_kr=beer[1],
                    brew_name=beer[2],
                    country=beer[3],
                    category=beer[4],
                    style=beer[5],
                    abv=beer[6],
                    image_file_name=beer[7]
                )

        return Response({'beer': beers},status=200)
    

@api_view(['GET'])
def recommendation(request):
    pk_list = random.sample(range(4,500),6)
    beers = Beer.objects.filter(pk__in=pk_list)
    for beer in beers:
        beer.image_url = getURL(beer.image_file_name)
    serializer = BeerSerializer(beers, many=True)
    return Response(serializer.data)