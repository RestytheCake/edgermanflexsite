from django import template
from django.contrib.auth.models import User

from ..models import forum

register = template.Library()


@register.simple_tag()
def msg():
    return str(forum)

@register.simple_tag()
def get_user(username):
    try:
        user = User.objects.get(username__iexact=username)
    except User.DoesNotExist:
        user = User.objects.none()
    return user

register.filter('get_user',get_user)

