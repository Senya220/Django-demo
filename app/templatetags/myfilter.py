from django import template

#custom define filters
register = template.Library()

@register.filter
def test_filter(value,args):
    return value * args
