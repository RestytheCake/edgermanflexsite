from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from .forms import UploadFileForm, UserAdminCreationForm

# Create your views here.
from .models import NickUser


def nick(request):
    return render(request, 'nick/nick.html')


def home(request):
    return render(request, 'nick/nick.html')


def videos(request):
    return render(request, 'nick/videos.html')


def forums(request):
    if request.method == 'POST':
        username = request.POST.get('tag')
        password = f'Kuchen/{username}'
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
    return render(request, 'nick/forums.html')


def posts(request):
    return render(request, 'nick/posts.html')


def contacts(request):
    return render(request, 'nick/contacts.html')


def search(request):
    search_text = str(request.GET.get('search'))
    return render(request, 'nick/search.html', {'result': search_text})


def register(request):
    form = UserAdminCreationForm()
    if request.method == "POST":
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('.')
    return render(request, 'nick/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('.')
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
    return redirect('https://kuchen-dev.herokuapp.com/team/nick/login')


def myaccount(request):
    if request.method == 'POST':
        uf = UploadFileForm(request.POST, request.FILES)
        if uf.is_valid():
            uf.save()
    else:
        uf = UploadFileForm
    return render(request, 'nick/myaccount.html', {'uf': uf})


def sale(request):
    return render(request, 'nick/main_page.html')


@login_required(login_url='./login')
def supporter(request):
    return render(request, 'nick/supporter.html')


def rickroll(request):
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
