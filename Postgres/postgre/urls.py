from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('',index),
    # URL для страницы входа (login)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # URL для страницы выхода (logout)
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('chart/', chart_view, name='line_chart'),
    path('director_dashboard/', views.director_dashboard, name='director_dashboard'),

]