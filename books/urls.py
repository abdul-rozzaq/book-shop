from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('cart/', cart_page, name='cart'),
    path('detail/<int:pk>/', detail_page, name='detail'),
]