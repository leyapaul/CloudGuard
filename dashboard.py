import json


with open("alerts/security_alerts.json", "r") as file:
    alerts = json.load(file)


critical = 0
high = 0


for alert in alerts:

    if alert["severity"] == "CRITICAL":
        critical += 1

    elif alert["severity"] == "HIGH":
        high += 1


print("\n====== CLOUDGUARD SECURITY DASHBOARD ======")

print(f"\nTotal Alerts: {len(alerts)}")

print(f"🚨 Critical Alerts: {critical}")

print(f"⚠️ High Alerts: {high}")


print("\nDetected Threats:")

for alert in alerts:

    print("--------------------------------")
    print("Time:", alert["time"])
    print("User:", alert["user"])
    print("Event:", alert["event"])
    print("Severity:", alert["severity"])
    print("Risk:", alert["risk"])