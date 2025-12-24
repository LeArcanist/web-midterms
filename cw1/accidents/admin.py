from django.contrib import admin
from .models import Accident

@admin.register(Accident)
class AccidentAdmin(admin.ModelAdmin):
    list_display = ("id", "crash_date", "weather_condition", "most_severe_injury", "injuries_total")
    search_fields = ("prim_contributory_cause", "weather_condition", "lighting_condition")
    list_filter = ("weather_condition", "lighting_condition", "most_severe_injury", "crash_month")
