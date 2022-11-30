from django.urls import path
from .views import index
urlpatterns = [
    # #http:localhost:8000
    # path('', index),
    # http:localhost:8000/index
    #first  http://127.0.0.1:8000/index?name=guan&age=10
    # path('index',index),
    #second  http://127.0.0.1:8000/index/name=guan&age=10
    path('index/<str:name>/<int:age>', index),
]
