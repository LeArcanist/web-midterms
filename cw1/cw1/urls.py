from django.contrib import admin
from django.urls import path, include
from accidents.views_home import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("accidents.urls")),
]

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("accidents.urls")),
]