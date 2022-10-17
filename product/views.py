from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import views
from .models import Product, Country
from product import serializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint' : '/notes/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of notes',
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = serializers.ProductSerializer(products, many=True, context={"request": request})
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = serializers.ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    data = request.data

    product = Product.objects.create(
        name=data['name'],
        price = data['price'],
        qauntity = data['qauntity'],
        country = data['country'],
        address = data['address'],
        description = data['description'],
        user = data['user'],
        image =  data['image'],
    )
    serializer = serializers.ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(id=pk)
    serializer = serializers.ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product was deleted.')
    
@api_view(['GET'])
def getCountries(request):
    countries = Country.objects.all()
    serializer = serializers.CountrySerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCountry(request, pk):
    country = Country.objects.get(id=pk)
    serializer = serializers.CountrySerializer(country, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createCountry(request):
    data = request.data
    country = Country.objects.create(
        name=data['name']
    )
    serializer = serializers.CountrySerializer(country, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateCountry(request, pk):
    data = request.data
    
    country = Country.objects.get(id=pk)
    serializer = serializers.CountrySerializer(country, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteCountry(request, pk):
    country = Country.objects.get(id=pk)
    country.delete()
    return Response('Country was deleted.')