from django.urls import path
from django.contrib import admin
from app import views
#class Message
from .views import Messgae,Index,Para,Calcu,Jinja,MessageTest,UserInfo

urlpatterns = {
    # #http:localhost:8000
    # path('', index),
    # http:localhost:8000/index
    # first  http://127.0.0.1:8000/index?name=guan&age=10
    # path('index',index),
    # second  http://127.0.0.1:8000/index/name=guan&age=10
    # path('index/<str:name>/<int:age>', index)
    path('admin/', admin.site.urls),
    path('get/', views.get),
    path('post/', views.post_html),
    path('result/', views.post),
    path('tpl/', views.tpl),
    path('news/', views.news),
    # http://127.0.0.1:8000/message/
    path('message/<str:name>/<int:age>', Messgae.as_view()),
    # #http://127.0.0.1:8000/
    # path('', Index.as_view()),
    # http://127.0.0.1:8000/index
    path('index', Index.as_view()),
    #http://127.0.0.1:8000/para  para is the name of param of get function in Para(View) ->list
    path('<str:name>', Para.as_view(), name='para'),
    path('calcu/', Calcu.as_view()),
    path('jinja/',Jinja.as_view()),
    #http://127.0.0.1:8000/message/info?message_type=info
    path('message/<str:message_type>', MessageTest.as_view()),
    path('userinfo/',UserInfo.as_view())

}
