from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

urlpatterns = [
    path('login/', LoginView.as_view(template_name= 'myapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name= 'register'),
    
] 