from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name=""),

    path('signupPage',views.signupPage, name="signupPage"),
    
    path('loginPage',views.loginPage, name="loginPage"),

    path('dashboard',views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),


]
