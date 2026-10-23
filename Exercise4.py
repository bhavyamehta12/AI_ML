logs = [
    {"service": "auth", "endpoint": "/login", "status": 200, "duration_ms": 120},
    {"service": "payments", "endpoint": "/checkout", "status": 500, "duration_ms": 900},
    {"service": "auth", "endpoint": "/login", "status": 401, "duration_ms": 200},
    {"service": "products", "endpoint": "/products", "status": 200, "duration_ms": 80},
    {"service": "payments", "endpoint": "/refund", "status": 503, "duration_ms": 1200},
    {"service": "auth", "endpoint": "/profile", "status": 200, "duration_ms": 600},
]
res = analyze_logs(logs)
def analyze_logs(
    logs,
    allowed_services=None,
    *,
    slow_threshold_ms=500,
    limit=None
):
    if slow_threshold_ms>0 and limit>0 and logs==[]:
        if not isinstance(logs, list):
            raise TypeError("logs must be a list")
