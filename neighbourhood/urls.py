from django.urls import path

from neighbourhood import views

urlpatterns = [
    path('',views.neighbour_view,name="neighbourhood"),
    path('myhood',views.get_neighbourhood,name="myhood"),
    path('business/',views.business_view,name="business"),
    path('occurence/<int:pk>',views.occurence_view,name="occurence"),
    path('join_hood/<int:pk>',views.join_neighbourhood,name="joinhood")
]