from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import views

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