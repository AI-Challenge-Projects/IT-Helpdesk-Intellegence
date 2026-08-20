from priority import get_priority

def test_urgent_keyword_gives_high_priority():
    assert get_priority("the system is down") == "High"

def test_normal_ticket_gives_medium_priority():
    assert get_priority("please update my email signature") == "Medium"