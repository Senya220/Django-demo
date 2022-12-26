from django.db import models
import json
from functools import wraps
from django_redis import get_redis_connection

#cache
_cache = get_redis_connection('default')
def cache(func):
    @wraps(func)
    def wrapper(obj,*args):
        key = args[0]
        value = _cache.get(key)
        if value:
            #convert to dict
            return json.loads(value)
        rs = func(obj,*args)
        _cache.set(key,json.dumps(rs))
        return rs
    return wrapper


# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女')
    )

    name = models.CharField(max_length=30, unique=True, verbose_name='姓 名')
    birthday = models.DateField(blank=True, null=True, verbose_name='生 日')
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, verbose_name='性 别')
    account = models.IntegerField(default=0, verbose_name='工 号')
    age = models.IntegerField(default=18, verbose_name='年 龄')
    info = models.CharField(default='dd',max_length=30,verbose_name='info')

class Userinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True,max_length=20,blank=False)
    age = models.SmallIntegerField(default=0)
    phone = models.SmallIntegerField(db_index=True,blank=True,default=0)
    email = models.EmailField(blank=True,default='')
    info = models.TextField()

    #add time when create
    create_time = models.DateTimeField(auto_now_add=True)
    #update time when update info
    update_time = models.DateTimeField(auto_now=True)

    #union index
    class Meta:
        index_together = ['username','phone']

class Userprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.SET_NULL)
    birthday = models.CharField(max_length=50,blank=True,default='')

#1:n
class Userlog(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,related_name='user_log',on_delete=models.SET_NULL,blank=True,null=True)
    content = models.TextField()
    create_time = models.DateTimeField()


#n:n
class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ManyToManyField(User,related_name='group')
    name = models.CharField(max_length=20)
    create_time = models.IntegerField(default=0)


class userIn(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    @classmethod
    @cache
    def get(cls, id):
        rs = cls.objects.get(id=id)
        return {
            # 'id': rs.id,
            'name': rs.name,
            'age': rs.age,
            'info': rs.info,
            'create_time': str(rs.create_time),
            'update_time': str(rs.update_time)
        }



class Auth(models.Model):
    username = models.CharField(max_length=18,verbose_name='用户名')
    password = models.CharField(max_length=18,verbose_name='密码')
































