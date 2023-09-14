from django.urls import path,include
from . import views 

urlpatterns = [
    #path('homepage',views.homepage,name='posts_home'),
    #path('homepage',views.homepage,name='posts_home'),
    #path('',views.list_posts,name='list_posts'),
    #path('<int:post_id>',views.post_detail,name='post_detail'),
    #path('update/<int:post_id>/',views.update_post,name='update_post'),
    #path('delete/<int:post_id>/',views.delete_post,name='delete_post')
    path('',views.PostListCreate.as_view(),name='list_posts'),
    path('<str:title>/',views.buscar_por_titulo,name='buscar_por_titulo')
]


