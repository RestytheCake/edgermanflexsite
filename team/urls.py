from . import views
from django.urls import path

app_name = 'team'
urlpatterns = [
    path('', views.nick, name='home'),
    path('/videos/', views.videos, name='video'),
    # Forum
    path('/forum/', views.forum_view, name='forum'),
    path('/forum/comment/', views.comment_view, name='comment'),
    path('/forum/create', views.forum_create, name='create'),
    path('/forum/search/', views.search_post, name='message_search'),
    path('/forum/filter', views.advfilter, name='advfilter'),
    path('/forum/searchworker/', views.searchworker_view, name='searchworker'),
    # Forum End
    path('/posts/', views.posts, name='posts'),
    path('/contact/', views.contacts, name='contact'),
    # Profile
    path('/profile/', views.profile_view, name='profile'),
    path('/profile/fa/', views.fa, name='fa'),
    path('/profileadd', views.profile_add, name='profile_add'),
    path('/notification', views.notification_view, name='notification'),
    path('/settings', views.settings_view, name='settings'),
    # Account
    path('/login/', views.login_view, name='login_view'),
    path('/register/', views.register, name='register'),
    path('/logout/', views.logout_view, name='logout'),
    # Old Site
    path('/sale/', views.sale, name='sale'),
    # For Supporter
    path('/supporter/', views.supporter, name='supporter'),
    # Help
    path('/problems', views.problems, name='problem'),
    # Rickroll
    path('/tests', views.rickroll, name='rickroll'),

]
