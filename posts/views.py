from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

class PostListCreate(APIView):
    serializer_class = PostSerializer
    
    def get(self,request:Request,*args,**kwargs):
        posts = Post.objects.all()
        
        serializer = self.serializer_class(instance=posts,many=True)
        response = {'message':'Posts','data':serializer.data}
        
        return Response(data=response,status=status.HTTP_200_OK)
    def post(self,request:Request,*args,**kwargs):
        data = request.data
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
"""
posts = [
    {'id':1,'title':'London park','description':'Lorem ipsun dolor, make'},
    {'id':2,'title':'Building','description':'Lorem ipsun dolor, make'},
    {'id':3,'title':'Materializer','description':'Lorem ipsun dolor, make'}
]
# Create your views here.

@api_view(http_method_names=['GET','POST'])
def homepage(request:Request):
    post = Post.objects.all()
    
    if request.method == 'POST':
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            response = {
            'message':'Post created',
            'data':serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    serializer = PostSerializer(instance=post,many=True)
    response = {'message':'Posts','data':serializer.data}
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def list_posts(request:Request):
    data = posts
    response = {'message':'Sucesso','data':data}
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def post_detail(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    
    serializer = PostSerializer(instance=post)
    
    response = {
        'message':"Post",
        'data':serializer.data
    }
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=['PUT'])
def update_post(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    
    data = request.data
    serializer = PostSerializer(instance=post,data=data)
    
    if serializer.is_valid():
        serializer.save()
        
        response = {
            'message':'Updated post successfuly',
            'data':serializer.data
        }
        
        return Response(data=response,status=status.HTTP_200_OK)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['DELETE'])
def delete_post(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    
    post.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)
        
        
"""       