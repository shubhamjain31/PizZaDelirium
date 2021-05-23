from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('' ,home, name='home' ),
    path('login', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('orders', orders_view, name='orders'),
    url(r'^(?P<id>\d+)/order', order_view, name='order'),
    path('api/order' , order_pizza , name='order_pizza'),
]