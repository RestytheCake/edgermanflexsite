from django import template

from ..models import profile

register = template.Library()


@register.simple_tag()
def fcheck(user, request_user):
    friends_data = profile.objects.filter(username__username=user)
    friendtest = 'nothing'
    for friends in friends_data:
        for list in friends.friend_list.all():
            if str(request_user) == str(list):
                friendtest = 'great'
            else:
                pass
    if friendtest == 'great':
        return 'You are already friends with this User'
    else:
        return 'Click here to send this User a Friend request'
