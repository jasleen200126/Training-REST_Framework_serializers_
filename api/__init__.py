from rest_framework.response import Response #it take any serialise data and send respose into json data
from rest_framework.decorators import api_view
#we are using function based view 

@api_view(['GET'])
def getData(request):
    person = {'name':'Dennis' , 'age':28}
    return Response()