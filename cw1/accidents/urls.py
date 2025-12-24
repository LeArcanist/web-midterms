from django.urls import path
from . import views

urlpatterns = [
    path("accidents/", views.AccidentListCreate.as_view(), name="accident-list-create"),
    path("accidents/<int:pk>/", views.AccidentDetail.as_view(), name="accident-detail"),

    path("accidents/alcohol/weekend/", views.AlcoholWeekendAccidents.as_view(), name="alcohol-weekend"),
    path("accidents/severe/", views.SevereAccidents.as_view(), name="severe"),
    path("accidents/intersections/multi-vehicle/", views.IntersectionMultiVehicle.as_view(), name="intersection-multi"),
    path("accidents/stats/weather/", views.AccidentCountsByWeather.as_view(), name="stats-weather"),
]
