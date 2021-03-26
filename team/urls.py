from . import views
from django.urls import path

app_name = 'team'
urlpatterns = [
    path('nick/', views.nick, name='nick'),
    path('nick/videos/', views.videos, name='videos'),
    path('nick/forum/', views.forum_view, name='forums'),
    path('nick/forum/create', views.forum_create, name='create'),
    path('nick/forum/search/', views.search_post, name='message_search'),
    path('nick/forum/filter', views.advfilter, name='advfilter'),
    path('nick/forum/profile/', views.profile_view, name='profile'),
    path('nick/forum/message/', views.comment_view, name='comment'),
    path('nick/forum/profile/fa/', views.fa, name='fa'),
    path('nick/posts/', views.posts, name='posts'),
    path('nick/contact/', views.contacts, name='contacts'),
    path('nick/login/', views.login_view, name='login_view'),
    path('nick/register/', views.register, name='register'),
    path('nick/result/', views.search, name='search'),
    path('nick/logout/', views.logout_view, name='logout'),
    path('nick/myaccount/', views.myaccount, name='myacount'),
    path('nick/sale/', views.sale, name='sale'),
    path('nick/supporter/', views.supporter, name='supporter'),
    path('nick/tests', views.rickroll, name='rickroll'),

]