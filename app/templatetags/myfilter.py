from django import template
from app.consts import SensitiveWord

import jieba

#custom define filters
register = template.Library()

@register.filter
def test_filter(value,args):
    return value * args


@register.filter
def simple_check(value):
    #get input message and split to word list
    message = jieba.lcut(value)
    #check sensitive word include in list
    check = list(set(message)) & set(SensitiveWord)
    print("input message:".format(message))
    if check:
        return "message inclue sensitive word"
    return value


@register.filter(name='deep_check_message')
def deep_check(value):
    #get input message and split to word list
    message = jieba.lcut(value)
    new_message = []
    for m in message:
        if m in SensitiveWord:
            new_message.append('*')
        else:
            new_message.append(m)
    if new_message:
        value = ''.join(new_message)
    return value























