from django.urls import path
from .views import register, login, logout,profile_page

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile_page, name='profile_page'),

]