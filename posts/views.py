from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


posts = [
    {'id':1,'title':'London park','description':'Lorem ipsun dolor, make'},
    {'id':2,'title':'Building','description':'Lorem ipsun dolor, make'},
    {'id':3,'title':'Materializer','description':'Lorem ipsun dolor, make'}
]
# Create your views here.

@api_view(http_method_names=['GET','POST'])
def homepage(request:Request):
    if request.method == 'POST':
        data = request.data
        response = {'message':'Hello World!','data':data}
        return Response(data=response,status=status.HTTP_201_CREATED)
    
    response = {'message':'Hello World!'}
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def list_posts(request:Request):
    data = posts
    response = {'message':'Sucesso','data':data}
    return Response(data=response,status=status.HTTP_200_OK)
    