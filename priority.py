URGENT_KEYWORDS = ["down", "can't work", "urgent", "asap", "not working", "broken", "outage"]

def get_priority(ticket_text: str) -> str:
    text_lower = ticket_text.lower()
    for keyword in URGENT_KEYWORDS:
        if keyword in text_lower:
            return "High"
    return "Medium"