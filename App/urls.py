from django.urls import path
from .views import *


urlpatterns = [
    path('' ,home, name='home' ),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    # path('api/order' , order_pizza , name='order_pizza'),
    # path('<order_id>/' , order , name='order')
]