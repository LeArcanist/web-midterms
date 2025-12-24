from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Accident
from .serializers import AccidentSerializer

# 1) CRUD list + POST
class AccidentListCreate(generics.ListCreateAPIView):
    queryset = Accident.objects.all().order_by("-crash_date")
    serializer_class = AccidentSerializer

# 2) CRUD detail (GET/PUT/PATCH/DELETE)
class AccidentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer

# 3) Alcohol + weekend filter (example "interesting")
class AlcoholWeekendAccidents(APIView):
    def get(self, request):
        qs = Accident.objects.filter(
            prim_contributory_cause__icontains="ALCOHOL",
            crash_day_of_week__in=[1, 7],
        ).order_by("-crash_date")
        return Response(AccidentSerializer(qs, many=True).data)

# 4) Severe accidents
class SevereAccidents(APIView):
    def get(self, request):
        qs = Accident.objects.filter(
            most_severe_injury__in=["FATAL", "INCAPACITATING INJURY"]
        ).order_by("-crash_date")
        return Response(AccidentSerializer(qs, many=True).data)

# 5) Intersection + multi-vehicle
class IntersectionMultiVehicle(APIView):
    def get(self, request):
        qs = Accident.objects.filter(
            intersection_related=True,
            num_units__gte=3
        ).order_by("-crash_date")
        return Response(AccidentSerializer(qs, many=True).data)

# 6) Aggregate endpoint (counts by weather)
class AccidentCountsByWeather(APIView):
    def get(self, request):
        # returns [{"weather_condition": "...", "count": N}, ...]
        from django.db.models import Count
        rows = (Accident.objects
                .values("weather_condition")
                .annotate(count=Count("id"))
                .order_by("-count"))
        return Response(list(rows))
