from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('verify-email/<uidb64>/<token>/',verify_email,name='verify_email'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
