from application import get_operating_system

def test_get_operating_system():
    assert get_operating_system() == 'Windows'