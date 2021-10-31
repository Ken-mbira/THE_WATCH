from django.urls import path

from neighbourhood import views

urlpatterns = [
    path('',views.NeighbourhoodList.as_view(),name="neighbourhoods"),
    path('locations/',views.LocationsList.as_view(),name="locations")
]