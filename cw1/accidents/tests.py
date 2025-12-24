from django.urls import reverse
from rest_framework.test import APITestCase
from accidents.models import Accident
from datetime import datetime

class AccidentAPITests(APITestCase):
    def setUp(self):
        self.a = Accident.objects.create(
            crash_date=datetime(2023, 7, 29, 13, 0, 0),
            num_units=2,
            intersection_related=True,
            prim_contributory_cause="ALCOHOL",
            most_severe_injury="NO INDICATION OF INJURY",
            injuries_total=0,
            injuries_fatal=0,
            injuries_incapacitating=0,
            injuries_non_incapacitating=0,
            injuries_reported_not_evident=0,
            injuries_no_indication=0,
            crash_hour=13,
            crash_day_of_week=7,
            crash_month=7,
        )

    def test_list_accidents(self):
        res = self.client.get("/api/accidents/")
        self.assertEqual(res.status_code, 200)

    def test_detail_accident(self):
        res = self.client.get(f"/api/accidents/{self.a.id}/")
        self.assertEqual(res.status_code, 200)

    def test_alcohol_weekend(self):
        res = self.client.get("/api/accidents/alcohol/weekend/")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(res.data) >= 1)

    def test_weather_stats(self):
        res = self.client.get("/api/accidents/stats/weather/")
        self.assertEqual(res.status_code, 200)
