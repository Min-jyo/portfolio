from django.urls import path

from . import views

app_name = 'members'
urlpatterns = [
    path('login/', views.login_views, name='login'),
]