from django.db import models

class Accident(models.Model):
    crash_date = models.DateTimeField()

    traffic_control_device = models.CharField(max_length=60, blank=True)
    weather_condition = models.CharField(max_length=50, blank=True)
    lighting_condition = models.CharField(max_length=50, blank=True)
    first_crash_type = models.CharField(max_length=60, blank=True)
    trafficway_type = models.CharField(max_length=60, blank=True)
    alignment = models.CharField(max_length=60, blank=True)
    roadway_surface_cond = models.CharField(max_length=60, blank=True)
    road_defect = models.CharField(max_length=60, blank=True)
    crash_type = models.CharField(max_length=60, blank=True)

    intersection_related = models.BooleanField(default=False)

    damage = models.CharField(max_length=60, blank=True)
    prim_contributory_cause = models.CharField(max_length=120, blank=True)

    num_units = models.IntegerField()
    most_severe_injury = models.CharField(max_length=60, blank=True)

    injuries_total = models.IntegerField()
    injuries_fatal = models.IntegerField()
    injuries_incapacitating = models.IntegerField()
    injuries_non_incapacitating = models.IntegerField()
    injuries_reported_not_evident = models.IntegerField()
    injuries_no_indication = models.IntegerField()

    crash_hour = models.IntegerField()
    crash_day_of_week = models.IntegerField()
    crash_month = models.IntegerField()

    def __str__(self):
        return f"Accident {self.id} @ {self.crash_date}"
