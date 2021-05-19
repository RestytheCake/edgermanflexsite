from django import template
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

register = template.Library()


@register.simple_tag()
def find(user):
    try:
        token = Token.objects.get(user=user)
        print(token)
        return token
    except:
        token = Token.objects.create(user=user)
        print(token.key)
        return token.key
