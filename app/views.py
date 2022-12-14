from django.shortcuts import render
from django.http import HttpResponse
#common view
from django.views.generic import View
import requests
import datetime

# Create your views here.

def index(request,name,age):
    name = request.GET.get('name','')
    age = request.GET.get('age',10)
    print(name,age)
    return HttpResponse('hello django')

def get(request):
    context = {}
    # 通过request.GET['name']形式获取get表单内容
    # result为重定向到的result.html所使用的变量
    context['result'] = f"你搜索的内容为：{request.GET['q']}"
    return render(request, 'result.html', context)


def post_html(request):
    # 不能和get一样使用render_to_response必须使用render进行重定向，不然服务端不会设置csrf_token
    # return render_to_response('post.html')
    return render(request, 'post.html')


def post(request):
    context = {}
    # 通过request.GET['name']形式获取post表单内容
    # result为重定向到的result.html所使用的变量
    context['result'] = f"你搜索的内容为：{request.POST['q']}"
    return render(request, 'result.html', context)

def tpl(request):
    name = "Jamie"
    roles = {"administrator","ceo"}
    return render(request,'tpl.html',{"n1":name,"n2":roles})

def news(request):
    url = "http://www.chinaunicom.com.cn/api/article/otherNewsByIndex/2/63".encode("utf-8")
    res = requests.get(url)
    data_list = res.json()
    print("aws")
    print(data_list)

    #[{"news_id":2480,"news_title":"告全党全军全国各族人民书","post_time":"2022-11-30","news_summary":"","news_thumbnail":null,
    # "news_link":"/ddjs/202211/1669804685355083409.html","creater":null,"hits":0},{"news_id":2478,
    # "news_title":"习近平同古巴共产党中央委员会第一书记、古巴国家主席迪亚斯-卡内尔举行会谈","post_time":"2022-11-27",
    # "news_summary":"","news_thumbnail":null,"news_link":"/ddjs/202211/1669799035099004032.html",
    # "creater":null,"hits":0},{"news_id":2477,
    # "news_title":"习近平同刚果（金）总统齐塞克迪就中刚关系正常化50周年互致贺电",
    # "post_time":"2022-11-24","news_summary":"","news_thumbnail":null,
    # "news_link":"/ddjs/202211/1669618301164052972.html","creater":null,"hits":0},
    # {"news_id":2475,"news_title":"习近平向发展中国家科学院第16届学术大会暨第30届院士大会致贺信",
    # "post_time":"2022-11-21","news_summary":"","news_thumbnail":null,
    # "news_link":"/ddjs/202211/1669074869624001132.html","creater":null,"hits":0},
    # {"news_id":2474,"news_title":"从巴厘岛到曼谷，习主席让世界读懂中国",
    # "post_time":"2022-11-20","news_summary":"","news_thumbnail":null,
    # "news_link":"/ddjs/202211/1669074816121074619.html","creater":null,"hits":0}]

    return render(request,'news.html')

class Messgae(View):
    def get(self,request,name,age):
        print(dir(request))
        # name = request.GET.get('name','')
        # age = request.GET.get('age',10)
        #http://127.0.0.1:8000/message/    my name is age is 10
        #http://127.0.0.1:8000/message/?name=Selina&&age=18  my name is Selina age is 18
        #return HttpResponse("my name is {}  age is {}".format(name,age))    path('message/', Messgae.as_view()),

        #param from get(self,request,name,age)
        #http: // 127.0.0.1: 8000 / message / selina / 18
        return HttpResponse("my name is {}  age is {}".format(name,age))


class Index(View):
    def get(self,request):
        return render(request,'showInfo.html',{'name':'Selina','age':22})

class Para(View):
    def get(self,request,name):
        list_data = range(10)
        return render(request,'pata.html',{'name':name,'list_data':list_data})


class Calcu(View):
    def get(self,request):
        data = {}
        data['count'] = 20
        data['time'] = datetime.datetime.now()
        data['cut_str'] = 'hello-today'
        data['firstpig'] = 'hello-django'
        data['result'] = False
        data['if_none'] = None
        #data['if_none'] = ''  ->empty string ->print in html still a empty string not none!!!!!
        data['dict'] = [{'name':'Selina','age':22},{'name':'Ethan','age':35},{'name':'Jamie','age':5}]
        data['floatNUm'] = 3.2345
        data['join'] = range(10)
        data['VVV'] = "Kong erv"
        data['link'] = "this is www.baidu.com"
        data['html_str'] = '<div style="background-color:red;width:50px;height:50px"> </div>'
        data['future'] = data['time'] + datetime.timedelta(days=5)
        return render(request,'calcu.html',data)



class Jinja(View):
    def get(self,request):
        data = {'name':'selina','age':5}
        return render(request,'jin.html',data)


class MessageType(View):
    def get(self,request,message_type):
        data = {}
        try:
            message_type_obj = message_type
        except:
            data['error'] = 'no this type'
            return render(request, 'enumMsg.html', data)

        message = request.GET.get('message','')
        if not message:
            data['error'] = "can't be none"
            return render(request,'enumMsg.html',data)

        data['message'] = message
        data['message_type'] = message_type_obj
        return render(request, 'enumMsg.html', data)















