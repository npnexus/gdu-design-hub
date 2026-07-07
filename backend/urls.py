from django.urls import path
from backend.views import *

urlpatterns = [
    path('dashboard',dashboard,name='dash'),
    path('orders/list', order_list, name='order_list'),
    path('detail/<int:pk>/', order_detail, name='order_detail'),
    path('update/<int:pk>/', update_order, name='update_order'),
    path('delete/<int:pk>/', delete_order, name='delete_order'),
]