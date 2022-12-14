from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from .jinja_filter import jinja_test,simple_check,deep_check

def environment(**options):
    env = Environment(**options)
    env.globals.update({ #modify
        'static':staticfiles_storage.url,#static appeared,call url function
        'url':reverse #url  appeared,call reverse function
    })
    #custom filter
    env.filters['jinja_test'] = jinja_test
    env.filters['simple_check'] = simple_check
    env.filters['deep_check'] = deep_check

    return env #return env after modify