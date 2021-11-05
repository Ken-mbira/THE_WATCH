from django.urls import path

from neighbourhood import views

urlpatterns = [
    path('',views.neighbour_view,name="neighbourhood"),
    path('myhood/',views.get_neighbourhood,name="myhood"),
    path('business/',views.business_view,name="business"),
    path('occurence/<int:pk>',views.occurence_view,name="occurence"),
    path('join_hood/<int:pk>',views.join_neighbourhood,name="joinhood"),
    path('move_out/',views.move_out,name="move_out"),
    path('locations/',views.LocationList.as_view(),name="location"),
    path('business/<int:pk>',views.get_businesses,name="hoodBusiness"),
    path('myhood/<int:pk>',views.get_residents,name="residents"),
    path('search/<str:term>',views.search_business,name="search_business")
]