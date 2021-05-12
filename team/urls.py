from . import views
from django.urls import path

app_name = 'team'
urlpatterns = [
    path('team/nick/', views.nick, name='home'),
    path('team/nick/videos/', views.videos, name='video'),
    # Forum
    path('team/nick/forum/', views.forum_view, name='forum'),
    path('team/nick/forum/comment/', views.comment_view, name='comment'),
    path('team/nick/forum/create', views.forum_create, name='create'),
    path('team/nick/forum/search/', views.search_post, name='message_search'),
    path('team/nick/forum/filter', views.advfilter, name='advfilter'),
    path('team/nick/forum/searchworker/', views.searchworker_view, name='searchworker'),
    # Forum End
    path('team/nick/posts/', views.posts, name='posts'),
    path('team/nick/contact/', views.contacts, name='contact'),
    # Profile
    path('team/nick/profile/', views.profile_view, name='profile'),
    path('team/nick/profile/fa/', views.fa, name='fa'),
    path('team/nick/profileadd', views.profile_add, name='profile_add'),
    path('team/nick/notification', views.notification_view, name='notification'),
    path('team/nick/settings', views.settings_view, name='settings'),
    # Account
    path('team/nick/login/', views.login_view, name='login_view'),
    path('team/nick/register/', views.register, name='register'),
    path('team/nick/logout/', views.logout_view, name='logout'),
    # Old Site
    path('team/nick/sale/', views.sale, name='sale'),
    # For Supporter
    path('team/nick/supporter/', views.supporter, name='supporter'),
    # Help
    path('team/nick/problems', views.problems, name='problem'),
    # Rickroll
    path('team/nick/tests', views.rickroll, name='rickroll'),

]
