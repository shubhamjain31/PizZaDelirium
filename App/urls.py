from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('' ,home, name='home' ),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('orders', orders_view, name='orders'),
    path('order/<order_id>/', order_view, name='order'),
    path('api/order' , order_pizza , name='order_pizza'),
]

def get_absolute_url(self):
    return reverse('order',kwargs = {"pk": self.pk})