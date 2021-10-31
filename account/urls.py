from django.urls import path
from rest_framework.authtoken import views as special_views

from account import views

urlpatterns = [
    path('login', special_views.obtain_auth_token),
    path('users',views.UserList.as_view(),name="users"),
    path('users/<int:pk>',views.UserDetail.as_view(),name="user")
]