from django.urls import path

from users.views import login, logout, application, app_create

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('application', application, name='application'),
    path('create', app_create, name='create')
]