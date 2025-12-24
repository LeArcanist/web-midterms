import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from accidents.models import Accident
from django.db import connection

DT_FORMAT = "%m/%d/%Y %I:%M:%S %p"

def to_int(x, default=0):
    try:
        return int(x)
    except:
        return default

def to_bool_YN(x):
    return str(x).strip().upper() == "Y"

class Command(BaseCommand):
    help = "Load traffic_accidents_10k.csv into the database"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, default="traffic_accidents_10k.csv")

    def handle(self, *args, **options):
        print(">>> loader running: chunked mode v1")
        connection.close()
        connection.ensure_connection()
        self.stdout.write(f"DB vendor: {connection.vendor}, connected: {connection.connection is not None}")
        path = options["path"]
        created = 0

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            objs = []
            for row in reader:
                objs.append(Accident(
                    crash_date=datetime.strptime(row["crash_date"], DT_FORMAT),

                    traffic_control_device=row.get("traffic_control_device", "") or "",
                    weather_condition=row.get("weather_condition", "") or "",
                    lighting_condition=row.get("lighting_condition", "") or "",
                    first_crash_type=row.get("first_crash_type", "") or "",
                    trafficway_type=row.get("trafficway_type", "") or "",
                    alignment=row.get("alignment", "") or "",
                    roadway_surface_cond=row.get("roadway_surface_cond", "") or "",
                    road_defect=row.get("road_defect", "") or "",
                    crash_type=row.get("crash_type", "") or "",

                    intersection_related=to_bool_YN(row.get("intersection_related_i", "N")),

                    damage=row.get("damage", "") or "",
                    prim_contributory_cause=row.get("prim_contributory_cause", "") or "",

                    num_units=to_int(row.get("num_units", 0)),
                    most_severe_injury=row.get("most_severe_injury", "") or "",

                    injuries_total=to_int(row.get("injuries_total", 0)),
                    injuries_fatal=to_int(row.get("injuries_fatal", 0)),
                    injuries_incapacitating=to_int(row.get("injuries_incapacitating", 0)),
                    injuries_non_incapacitating=to_int(row.get("injuries_non_incapacitating", 0)),
                    injuries_reported_not_evident=to_int(row.get("injuries_reported_not_evident", 0)),
                    injuries_no_indication=to_int(row.get("injuries_no_indication", 0)),

                    crash_hour=to_int(row.get("crash_hour", 0)),
                    crash_day_of_week=to_int(row.get("crash_day_of_week", 0)),
                    crash_month=to_int(row.get("crash_month", 0)),
                ))

            
            # --- Force SQLite connection to actually exist ---
            connection.close()
            connection.ensure_connection()
            with connection.cursor():
                pass

            # --- Insert in safe chunks (avoids Django sqlite getlimit bug) ---
            BATCH = 200
            created = 0

            for i in range(0, len(objs), BATCH):
                Accident.objects.bulk_create(objs[i:i+BATCH])
                created += len(objs[i:i+BATCH])

        self.stdout.write(self.style.SUCCESS(f"Loaded {created} accidents from {path}"))
