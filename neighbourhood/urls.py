from django.urls import path

from neighbourhood import views

urlpatterns = [
    path('',views.neighbour_view,name="neighbourhood")
]