import csv
from datetime import datetime

vibration = float(input("Vibration reading: "))

with open("motor_log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([datetime.now(), vibration])

if vibration > 5:
    print("Inspect motor: vibration threshold exceeded")
else:
    print("Reading logged")
