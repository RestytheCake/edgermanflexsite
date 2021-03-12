from django import template
from django.contrib.auth.models import User

from ..models import forum

register = template.Library()


@register.simple_tag()
def check(tags):
    try:
        tag = tags.split(' ')
        new_tag = ' '
        for singletag in tag:
            if singletag.startswith('#'):
                new_tag = f'{new_tag} {singletag}'
            else:
                new_tag = f'{new_tag} #{singletag}'
        return new_tag

    except:
        if tags.startswith('#'):
            return (tags)
        else:
            x = f'#{tags}'
            return x


