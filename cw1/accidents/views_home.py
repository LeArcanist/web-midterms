import platform
import sys
import django
import rest_framework
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "python_version": sys.version.split()[0],
        "django_version": django.get_version(),
        "drf_version": rest_framework.VERSION,
        "os": f"{platform.system()} {platform.release()}",
        
        "admin_user": "pzy10",
        "admin_pass": "123456",  
        "api_links": [
            ("/api/accidents/", "List/Create accidents (GET/POST)"),
            ("/api/accidents/1/", "Accident detail (GET/PUT/PATCH/DELETE)"),
            ("/api/accidents/alcohol/weekend/", "Alcohol + weekend filter"),
            ("/api/accidents/severe/", "Severe accidents"),
            ("/api/accidents/intersections/multi-vehicle/", "Intersection + multi-vehicle"),
            ("/api/accidents/stats/weather/", "Stats: counts by weather"),
        ],
        "admin_link": "/admin/",
        "how_to_run": [
            "pip install -r requirements.txt",
            "python manage.py migrate",
            "python manage.py load_accidents --path traffic_accidents_10k.csv",
            "python manage.py runserver",
            "python manage.py test",
        ],
    }
    return render(request, "home.html", context)
