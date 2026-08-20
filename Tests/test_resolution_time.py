from resolution_time import estimate_resolution_hours

def test_high_priority_cuts_time_in_half():
    assert estimate_resolution_hours("Hardware", "High") == 2.0

def test_medium_priority_uses_base_time():
    assert estimate_resolution_hours("Software", "Medium") == 2.0

def test_unknown_category_uses_default():
    assert estimate_resolution_hours("Mystery", "Medium") == 3.0