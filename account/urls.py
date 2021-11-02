from django.urls import path
from rest_framework.authtoken import views as special_views

from account import views

urlpatterns = [
    path('login', special_views.obtain_auth_token),
    path('register',views.register_view,name="register")
]