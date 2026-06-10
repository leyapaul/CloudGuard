HIGH_RISK_EVENTS = {

    "AttachUserPolicy": {
        "risk": "Privilege escalation attempt detected",
        "severity": "CRITICAL"
    },

    "CreateUser": {
        "risk": "New IAM user created",
        "severity": "HIGH"
    },

    "CreateAccessKey": {
        "risk": "New access key created",
        "severity": "HIGH"
    },

    "DeleteTrail": {
        "risk": "CloudTrail deletion attempt",
        "severity": "CRITICAL"
    },

    "StopLogging": {
        "risk": "CloudTrail logging stopped",
        "severity": "CRITICAL"
    }
}