import json
from datetime import datetime
from rules import HIGH_RISK_EVENTS


LOG_FILE = "logs/cloudtrail.json"


def load_logs():
    with open(LOG_FILE, "r") as file:
        return json.load(file)


def analyze_events(events):

    alerts = []

    for event in events["Records"]:

        event_name = event.get("eventName")
        user = event.get("userIdentity", {}).get("userName", "Unknown")
        time = event.get("eventTime")

        if event_name in HIGH_RISK_EVENTS:

            alert = {
                "time": time,
                "user": user,
                "event": event_name,
                "risk": HIGH_RISK_EVENTS[event_name]["risk"],
                "severity": HIGH_RISK_EVENTS[event_name]["severity"]
            }

            alerts.append(alert)

    return alerts


def save_alerts(alerts):

    filename = "alerts/security_alerts.json"

    with open(filename, "w") as file:
        json.dump(alerts, file, indent=4)


if __name__ == "__main__":

    print("🔍 CloudGuard scanning AWS logs...")

    logs = load_logs()

    results = analyze_events(logs)

    save_alerts(results)

    print(f"🚨 {len(results)} security alerts generated")

    for alert in results:
        print(alert)