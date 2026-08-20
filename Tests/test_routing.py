from routing import get_team

def test_hardware_routes_to_desktop_support():
    assert get_team("Hardware") == "Desktop Support"

def test_unknown_category_routes_to_general_support():
    assert get_team("Alien Technology") == "General Support"