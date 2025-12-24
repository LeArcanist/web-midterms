from rest_framework import serializers
from .models import Accident

class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = "__all__"

    def validate_crash_hour(self, value):
        if not 0 <= value <= 23:
            raise serializers.ValidationError("crash_hour must be 0..23")
        return value

    def validate_crash_day_of_week(self, value):
        if not 1 <= value <= 7:
            raise serializers.ValidationError("crash_day_of_week must be 1..7")
        return value
