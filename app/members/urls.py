from django.urls import path

from members import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('member/<int:pk>/', views.member_detail, name='member_detail'),
    path('member/new/', views.member_new, name='member_new'),
]