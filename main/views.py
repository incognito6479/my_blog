from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm, PostForms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import MakePost
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from decorators import anonymous_required
from django.core.paginator import Paginator


def main(request):
    lst = MakePost.objects.all()
    paginator = Paginator(lst, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'settings': settings,
        'page_obj': page_obj
    }
    return render(request, 'layout.html', context)


@anonymous_required(redirect_url='main:main')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                User.objects.get(email=request.POST['email'])
                form = SignupForm(request.POST)
                errors = _('This email is already exists, type in another email')
                return render(request, 'signup.html', {'forms': form, 'error': errors})
            except:
                user = User.objects.create_user(username=request.POST['login'],
                                                email=request.POST['email'],
                                                password=request.POST['password'],
                                                last_name=request.POST['name'])
                user.save()
                return redirect('main:login')
        else:
            form = SignupForm(request.POST)
            return render(request, 'signup.html', {'forms': form})

    form = SignupForm()
    return render(request, 'signup.html', {'forms': form})


@anonymous_required(redirect_url='main:main')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth = authenticate(username=request.POST['login'], password=request.POST['password'])
            if auth is not None:
                login(request, auth)
                return redirect('main:main')
            else:
                errors = _('Login or password is incorrect')
                return render(request, 'login.html', {'errors': errors, 'forms': form})
        else:
            form = LoginForm()
            return render(request, 'login.html', {'forms': form})

    form = LoginForm()
    return render(request, 'login.html', {'forms': form})


@login_required
def my_account(request):
    form = PostForms()
    return render(request, 'account.html', {'form': form})


@login_required
def upload(request):
    form = PostForms(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.post_user = request.user.last_name
        obj.save()
        return redirect('main:main')
    return render(request, 'account.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('main:main')


@login_required
def show_user_post(request):
    user_posts = MakePost.objects.filter(post_user=request.user.last_name)
    if request.method == 'POST' and request.POST.get('edit'):
        delete = MakePost.objects.get(id=request.POST['edit'])
        
    elif request.method == 'POST' and request.POST.get('delete'):
        delete = MakePost.objects.get(id=request.POST['delete'])
        if delete is not None:
            delete.delete()

    paginator = Paginator(user_posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'user_posts.html', {'page_obj': page_obj})
