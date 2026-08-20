TEAM_ROUTING = {
    "Hardware": "Desktop Support",
    "Software": "Application Support",
    "Network": "Infrastructure Team",
    "Access": "IT Security",
}

def get_team(category: str) -> str:
    return TEAM_ROUTING.get(category, "General Support")

