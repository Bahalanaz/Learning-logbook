# Day 15 — FleetFlow
The culmination of this 15-day learning journey.
FleetFlow is a production-style delivery fleet management REST API 
built with Django 6 and PostgreSQL.
Features:
- JWT authentication with 3-role custom permissions
- 8-state order lifecycle state machine with enforced transitions
- Service layer using transaction.atomic() and select_for_update()
- Event-driven audit logs, tracking events, and notifications
- 6 modular Django apps
🔗 Full project: https://github.com/Bahalanaz/FleetFlow