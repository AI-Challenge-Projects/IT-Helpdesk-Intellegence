BASE_HOURS = {
    "Hardware": 4,
    "Software": 2,
    "Network": 6,
    "Access": 1,
}

def estimate_resolution_hours(category: str, priority: str) -> float:
    base = BASE_HOURS.get(category, 3)
    if priority == "High":
        return round(base * 0.5, 1)
    return float(base)