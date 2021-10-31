from django.urls import path

from neighbourhood import views

urlpatterns = [
    path('',views.NeighbourhoodList.as_view(),name="neighbourhoods"),
    path('<int:pk>',views.NeighbourhoodDetail.as_view(),name="single_neighbourhood"),
    path('locations/',views.LocationsList.as_view(),name="locations"),
    path('profiles',views.ProfilesList.as_view(),name="profiles"),
    path('profiles/<int:pk>',views.ProfileDetail.as_view(),name="profile"),
    path('business',views.BusinessList.as_view(),name="businesses"),
    path('business/<int:pk>',views.BusinessDetail.as_view(),name="business"),
    path('services',views.ServicesList.as_view(),name="services")
]