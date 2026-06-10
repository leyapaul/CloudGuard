# CloudGuard - AWS Security Monitoring Tool 

CloudGuard is a Python based AWS security monitoring project that analyzes AWS CloudTrail logs and detects risky cloud activities.

## Features

- Parses AWS CloudTrail JSON logs
- Detects high risk IAM activities
- Identifies privilege escalation attempts
- Generates security alerts
- Creates JSON alert reports
- Exports CSV security reports
- Provides a terminal security dashboard

## Detected Threats

🚨 Critical:
- AttachUserPolicy
- CreateAccessKey

⚠️ High:
- CreateUser

## Tech Stack

- Python
- AWS IAM
- AWS CloudTrail
- JSON
- CSV

## Project Workflow

AWS CloudTrail Logs
        ↓
Python Detection Engine
        ↓
Threat Analysis
        ↓
Security Alerts
        ↓
JSON + CSV Reports


## Output Example

Total Alerts: 5

Critical Alerts: 3

High Alerts: 2


## Purpose

This project demonstrates basic Cloud Security Monitoring and SIEM concepts using AWS logs.