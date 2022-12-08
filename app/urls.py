from django.urls import path
from django.contrib import admin
from app import views
# from .views import index

urlpatterns = [
    # #http:localhost:8000
    # path('', index),
    # http:localhost:8000/index
    #first  http://127.0.0.1:8000/index?name=guan&age=10
    # path('index',index),
    #second  http://127.0.0.1:8000/index/name=guan&age=10
    # path('index/<str:name>/<int:age>', index)
    path('admin/', admin.site.urls),
    path('get/', views.get),
    path('post/', views.post_html),
    path('result/', views.post),
    path('tpl/', views.tpl),
    path('news/', views.news),

]
