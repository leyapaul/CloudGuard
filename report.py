import json
import csv


with open("alerts/security_alerts.json", "r") as file:
    alerts = json.load(file)


with open("alerts/security_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Time",
        "User",
        "Event",
        "Severity",
        "Risk"
    ])

    for alert in alerts:
        writer.writerow([
            alert["time"],
            alert["user"],
            alert["event"],
            alert["severity"],
            alert["risk"]
        ])


print("✅ Security report generated successfully!")