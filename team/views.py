from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from allauth.socialaccount.models import SocialAccount

# Create your views here.
from .models import NickUser, forum, notification, profile, comment
from .forms import addforum, commentform, notify, profileform, UploadFileForm, UserAdminCreationForm


def nick(request):
    return render(request, 'nick/nick.html')


def home(request):
    return render(request, 'nick/nick.html')


def videos(request):
    return render(request, 'nick/videos.html')


def forum_view(request):
    data = forum.objects.all().order_by('-created_at')
    form = addforum()
    likeobj = forum.objects.annotate(like_count=Count('like')).order_by('-like_count')[:3]
    if request.method == 'POST':
        form = addforum(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user.username
            instance.save()

    return render(request, 'nick/forum.html', {'message': data, 'form': form, 'likeobj': likeobj})


def forum_create(request):
    form = addforum()
    if request.method == 'POST':
        form = addforum(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            user = request.user.username
            post = forum.objects.filter(title=title, user=user)
            if post:
                noti = notify()
                instance = noti.save(commit=False)
                instance.User = request.user.username
                instance.Warning = 'Double Post'
                instance.Post_title = request.POST.get('title')
                instance.Post_message = request.POST.get('message')
                instance.Post_Tags = request.POST.get('tags')
                instance.Description = 'You have submitted a Post with a Title you already used'
                instance.Sender = 'System'
                instance.save()
            else:
                instance = form.save(commit=False)
                instance.user = request.user.username
                instance.save()
            return redirect('/team/nick/forum')
    return render(request, 'nick/forum_create.html', {'form': form})


def advfilter(request):
    return render(request, 'nick/advancedSRC.html')


def search_post(request):
    obj = ''
    if request.GET.get('searching'):
        getuser = request.GET.get('searching')
        obj = forum.objects.filter(user=getuser)
    if request.GET.get('user'):
        userget = request.GET.get('user')
        obj = forum.objects.filter(user__contains=userget)
        if request.GET.get('title'):
            titleget = request.GET.get('title')
            obj = forum.objects.filter(user__contains=userget, ).order_by('-created_at')
            if request.GET.get('keywords'):
                tagsget = request.GET.get('keywords')
                obj = forum.objects.filter(user__contains=userget, title__contains=titleget,
                                           tags__contains=tagsget).order_by('-created_at')
                if request.GET.get('date'):
                    dateget = request.GET.get('date')
                    obj = forum.objects.filter(user=userget, title__contains=titleget, tags__contains=tagsget,
                                               created_at=dateget).order_by('-created_at')
                    if request.GET.get('popularity'):
                        if request.GET.get('popularity') == 'mostlike':
                            obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
                        else:
                            obj = obj.annotate(like_count=Count('like')).order_by('like_count')
        elif request.GET.get('keywords'):
            tagsget = request.GET.get('keywords')
            obj = forum.objects.filter(user__contains=userget, tags__contains=tagsget).order_by('-created_at')
            if request.GET.get('date'):
                dateget = request.GET.get('date')
                obj = forum.objects.filter(user=userget, tags__contains=tagsget, created_at=dateget).order_by(
                    '-created_at')
                if request.GET.get('popularity'):
                    if request.GET.get('popularity') == 'mostlike':
                        obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
                    else:
                        obj = obj.annotate(like_count=Count('like')).order_by('like_count')
        elif request.GET.get('date'):
            dateget = request.GET.get('date')
            obj = forum.objects.filter(user=userget, created_at=dateget).order_by('-created_at')
            if request.GET.get('popularity'):
                if request.GET.get('popularity') == 'mostlike':
                    obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
                else:
                    obj = obj.annotate(like_count=Count('like')).order_by('like_count')
        elif request.GET.get('popularity'):
            if request.GET.get('popularity') == 'mostlike':
                obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
            else:
                obj = obj.annotate(like_count=Count('like')).order_by('like_count')
    elif request.GET.get('title'):
        titleget = request.GET.get('title')
        obj = forum.objects.filter(title__contains=titleget)
        if request.GET.get('keywords'):
            tagsget = request.GET.get('keywords')
            obj = forum.objects.filter(title__contains=titleget, tags__contains=tagsget)
            if request.GET.get('date'):
                dateget = request.GET.get('date')
                obj = forum.objects.filter(title__contains=titleget, tags__contains=tagsget, created_at=dateget)
                if request.GET.get('popularity'):
                    if request.GET.get('popularity') == 'mostlike':
                        obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
                    else:
                        obj = obj.annotate(like_count=Count('like')).order_by('like_count')
        elif request.GET.get('date'):
            dateget = request.GET.get('date')
            obj = forum.objects.filter(created_at=dateget).order_by('-created_at')
            if request.GET.get('popularity'):
                if request.GET.get('popularity') == 'mostlike':
                    obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
                else:
                    obj = obj.annotate(like_count=Count('like')).order_by('like_count')
        elif request.GET.get('popularity'):
            if request.GET.get('popularity') == 'mostlike':
                obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
            else:
                obj = obj.annotate(like_count=Count('like')).order_by('like_count')
    elif request.GET.get('keywords'):
        tagsget = request.GET.get('keywords')
        obj = forum.objects.filter(tags__contains=tagsget)
        if request.GET.get('date'):
            dateget = request.GET.get('date')
            obj = forum.objects.filter(created_at=dateget).order_by('-created_at')
            if request.GET.get('popularity'):
                if request.GET.get('popularity') == 'mostlike':
                    obj = obj.objects.annotate(like_count=Count('like')).order_by('-like_count')
                else:
                    obj = obj.objects.annotate(like_count=Count('like')).order_by('like_count')
        elif request.GET.get('popularity'):
            if request.GET.get('popularity') == 'mostlike':
                obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
            else:
                obj = obj.annotate(like_count=Count('like')).order_by('like_count')
    elif request.GET.get('date'):
        dateget = request.GET.get('date')
        date0 = str(dateget.split('-')[0])
        print(date0)
        date1 = str(dateget.split('-')[1])
        print(date1)
        date2 = str(dateget.split('-')[2])
        print(date2)
        obj = forum.objects.filter(created_at__year=date0, created_at__month=date1, created_at__day=date2)
        if request.GET.get('popularity'):
            if request.GET.get('popularity') == 'mostlike':
                obj = obj.annotate(like_count=Count('like')).order_by('-like_count')
            else:
                obj = obj.annotate(like_count=Count('like')).order_by('like_count')
    elif request.GET.get('popularity'):
        if request.GET.get('popularity') == 'mostlike':
            obj = forum.objects.annotate(like_count=Count('like')).order_by('-like_count')
        else:
            obj = forum.objects.annotate(like_count=Count('like')).order_by('like_count')
    return render(request, 'nick/message_search.html', {'search': obj})


def searchworker_view(request):
    user = request.GET.get('user')
    title = request.GET.get('title')
    url = f'/team/nick/forum/#{user}={title}'
    return redirect(url)



def profile_view(request):
    if request.GET.get('user'):
        usernameget = request.GET.get('user')
        profile_data = profile.objects.filter(username__username=usernameget)
        forum_data = forum.objects.filter(user=usernameget).order_by('-created_at')
        msg_counter = forum_data.count()
        friends_data = profile.objects.filter(username__username=usernameget)
        cc_data = comment.objects.filter(User=usernameget)
        cc_counter = cc_data.count()

    return render(request, 'nick/profile.html',
                  {'profile': profile_data, 'data': forum_data, 'msg_counter': msg_counter,'cc_counter': cc_counter ,'friend_data': friends_data,'cc_data': cc_data, 'user': usernameget})


def notification_view(request):
    notification_data = notification.objects.filter(User=request.user.username).order_by('-created_at')
    return render(request, 'nick/notification.html', {'notify': notification_data})

def fa(request):
    if request.GET.get('fa') == 'true':

        user = request.GET.get('user')
        user_request = request.GET.get('user_request')

        userobj = get_object_or_404(profile, username=user)
        user_requestobj = get_object_or_404(profile, username=user_request)
        user_id = get_object_or_404(get_user_model(), username=user)

        userobj.fa_list.add(request.user)
        user_requestobj.fa_send.add(user_id)

        return redirect(f'/team/nick/forum/profile/?user={user}')

    if request.GET.get('fa') == 'decline':
        user = request.GET.get('user')
        user_request = request.GET.get('user_request')

        userobj = get_object_or_404(profile, username=user)
        user_requestobj = get_object_or_404(profile, username=user_request)
        user_id = get_object_or_404(get_user_model(), username=user)

        userobj.fa_send.remove(request.user)
        user_requestobj.fa_list.remove(user_id)

        return redirect(f'/team/nick/forum/profile/?user={user}')

    if request.GET.get('fa') == 'accept':
        user = request.GET.get('user') #Resty
        user_request = request.GET.get('user_request') #whynot

        userobj = get_object_or_404(profile, username=user)  #Restyobj
        user_requestobj = get_object_or_404(profile, username=user_request)  #whynotobj
        user_id = get_object_or_404(get_user_model(), username=user) #Restyid

        userobj.fa_send.remove(request.user)
        user_requestobj.fa_list.remove(user_id)

        userobj.friend_list.add(request.user)
        user_requestobj.friend_list.add(user_id)

        return redirect(f'/team/nick/forum/profile/?user={user}')

    return redirect('/team/nick/')


def profile_add(request):
    if request.user.is_authenticated:
        userstuff = SocialAccount.uid.all()
        print(userstuff)
    return redirect('/team/nick/')


def comment_view(request):
    userget = request.GET.get('user')
    titleget = request.GET.get('title')
    form = commentform()
    if request.POST.get('comments'):
        if commentform(request.POST) != form:
            form = commentform(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.User = request.user.username
                instance.main_post_user = userget
                instance.main_post_title = titleget
                instance.save()
                return redirect(f'/team/nick/forum/message/?user={userget}&title={titleget}')
        else:
            pass
    if request.POST.get('like'):
        if request.user.is_authenticated:
            obj = get_object_or_404(forum, user=userget, title=titleget)
            obj.like.add(request.user)
        else:
            return redirect(
                f'/team/nick/login/?next=/team/nick/forum/message/?user={userget}&title={titleget}&reason=like')
    if request.POST.get('dislike'):
        if request.user.is_authenticated:
            obj = get_object_or_404(forum, user=userget, title=titleget)
            obj.dislike.add(request.user)
        else:
            return redirect(
                f'/team/nick/login/?next=/team/nick/forum/message/?user={userget}&title={titleget}&reason=like')
    if request.POST.get('unlike'):
        if request.user.is_authenticated:
            obj = get_object_or_404(forum, user=userget, title=titleget)
            obj.like.remove(request.user)
        else:
            return redirect(
                f'/team/nick/login/?next=/team/nick/forum/message/?user={userget}&title={titleget}&reason=like')
    if request.POST.get('undislike'):
        if request.user.is_authenticated:
            obj = get_object_or_404(forum, user=userget, title=titleget)
            obj.dislike.remove(request.user)
        else:
            return redirect(
                f'/team/nick/login/?next=/team/nick/forum/message/?user={userget}&title={titleget}&reason=like')
    if request.GET.get('user'):
        main_post_data = forum.objects.filter(user=userget, title=titleget)
        comment_data_old = comment.objects.filter(main_post_user=userget, main_post_title=titleget)
        comment_data_new = comment.objects.filter(main_post_user=userget, main_post_title=titleget).order_by(
            '-created_at')

    return render(request, 'nick/comment.html',
                  {'msg': main_post_data, 'comments_old': comment_data_old, 'comments_new': comment_data_new,
                   'form': form})


def posts(request):
    return render(request, 'nick/posts.html')


def contacts(request):
    return render(request, 'nick/contacts.html')


def search(request):
    search_text = str(request.GET.get('search'))
    return render(request, 'nick/search.html', {'result': search_text})


def register(request):
    form = UserCreationForm()
    pform = profileform()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                instance = pform.save(commit=False)
                instance.username = request.user
                instance.save()
                return redirect('/team/nick/')
    return render(request, 'nick/register.html', {'form': form})


def login_view(request):
    if request.GET.get('reason') == 'like':
        reasonlike1 = 'You are not logged in.'
        reasonlike2 = 'Log in to Like and Dislike Posts'
        if request.user.is_authenticated:
            return redirect('/team/nick')
        elif request.POST.get('username'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                next = f'{request.GET.get("next")}&title={request.GET.get("title")}'
                return redirect(next)
            else:
                return render(request, 'nick/login.html')
        else:
            return render(request, 'nick/login.html', {'reasonError1': reasonlike1, 'reasonError2': reasonlike2})
    if request.user.is_authenticated:
        return redirect('/team/nick')
    elif request.POST.get('username'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('.')
        else:
            return render(request, 'nick/login.html')
    else:
        return render(request, 'nick/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        pass
    return redirect('/team/nick/login')


def myaccount(request):
    if request.method == 'POST':
        uf = UploadFileForm(request.POST, request.FILES)
        if uf.is_valid():
            uf.save()
    else:
        uf = UploadFileForm
    return render(request, 'nick/myaccount.html', {'uf': uf})


def problems(request):
    return render(request, 'nick/problems.html')


def sale(request):
    return render(request, 'nick/main_page.html')


@login_required(login_url='./login')
def supporter(request):
    return render(request, 'nick/supporter.html')


def rickroll(request):
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


def angulartest(request):
    return render(request, 'nick/test.html')