from main import get_google_status

def test_get_google_status():
    assert get_google_status() == 200