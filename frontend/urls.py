from django.urls import path
from .views import *

urlpatterns = [
    path('',home_views,name='home'),
    path('start-your-project', create_order, name='startproject'),
    path('client-orders/', client_order_list, name='client_order_list'),
    path('orders-cancel/<int:pk>/', client_delete_order, name='client_delete_order'),   
]