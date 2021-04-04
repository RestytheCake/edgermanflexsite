from . import views
from django.urls import path
from rest_framework import routers


app_name = 'team'
urlpatterns = [
    path('team/nick/', views.nick, name='nick'),
    path('team/nick/videos/', views.videos, name='videos'),
    path('team/nick/forum/', views.forum_view, name='forums'),
    path('team/nick/forum/create', views.forum_create, name='create'),
    path('team/nick/forum/search/', views.search_post, name='message_search'),
    path('team/nick/forum/filter', views.advfilter, name='advfilter'),
    path('team/nick/forum/profile/', views.profile_view, name='profile'),
    path('team/nick/forum/message/', views.comment_view, name='comment'),
    path('team/nick/forum/profile/fa/', views.fa, name='fa'),
    path('team/nick/forum/profileadd', views.profile_add, name='profile_add'),
    path('team/nick/posts/', views.posts, name='posts'),
    path('team/nick/contact/', views.contacts, name='contacts'),
    path('team/nick/login/', views.login_view, name='login_view'),
    path('team/nick/register/', views.register, name='register'),
    path('team/nick/result/', views.search, name='search'),
    path('team/nick/logout/', views.logout_view, name='logout'),
    path('team/nick/myaccount/', views.myaccount, name='myacount'),
    path('team/nick/sale/', views.sale, name='sale'),
    path('team/nick/supporter/', views.supporter, name='supporter'),
    path('team/nick/tests', views.rickroll, name='rickroll'),

]