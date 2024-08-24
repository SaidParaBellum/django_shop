from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.forms import LoginForm, AppCreationForm
from users.models import TechSupport


# Create your views here.

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')

    return render(request, 'auth/login.html',
                  {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('index')


def application(request):
    limit = int(request.GET.get('limit', 5))
    page = int(request.GET.get('page', 1))
    offset = (page - 1) * limit
    applications = TechSupport.objects.all().order_by('solved', '-created_at')[offset:offset + limit]

    return render(request, 'tech/application.html', {
        'Applications': applications,
        'limit': limit,
        'page': page
    })
def app_create(request):
    form = AppCreationForm()
    if request.method == "POST":
        form = AppCreationForm(request.POST)
        if form.is_valid():
            form.save()



    return render(request, 'tech/app_create.html',
                  {'form': form})