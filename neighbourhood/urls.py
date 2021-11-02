from django.urls import path

from neighbourhood import views

urlpatterns = [
    path('',views.neighbour_view,name="neighbourhood"),
    path('business/',views.business_view,name="business"),
    path('occurence/<int:pk>',views.occurence_view,name="occurence")
]