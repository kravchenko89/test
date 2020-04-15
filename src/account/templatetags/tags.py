import django
from django import template
from django.template import Template
from django.template.defaultfilters import stringfilter

register = template.Library()


# @register.filter
# def change_tag(path):
#     path = 'hello'
#     return path

@register.simple_tag(takes_context=True)
def change_tag(context):
    return Template('<a href="http://127.0.0.1:8001/admin/account/user/{{ user.id }}">link</a>').render(context)

# # register.filter('change_tag', change_tag) {% request.user.id %}
