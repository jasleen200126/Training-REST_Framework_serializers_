import requests
from rest_framework.response import Response #it take any serialise data and send respose into json data
from rest_framework.decorators import api_view
from application.models import Item
from .serializers import ItemSerializer

#we are using function based view 

@api_view(['GET'])
def getData(request):
    item = Item.objects.all()
    serializer_data = ItemSerializer(item, many=True)

    return Response(serializer_data.data)

@api_view(['POST'])
def addItem(request):
    serializer_data = ItemSerializer(data= request.data)
    if serializer_data.is_valid():
        serializer_data.save()
    return Response()

# @api_view(['get'])
# def getFromUrl(request):
#     url = "https://api.freeapi.app/api/v1/public/randomusers"

#     query_params = {
#         "page": 1,
#         "limit": 10
#     }
#     data = request.get(url)

#     return Response(data)