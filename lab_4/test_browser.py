from main import wd, email, password, URL
import time

def test_log_in():
    wd.driver.get(URL)
    wd.login(email, password)
    time.sleep(4)
    assert wd.driver.current_url == f"{URL}/feed"

def test_get_dialogs_page():
    wd.get_dialog()
    time.sleep(4)
    assert wd.driver.current_url == f"{URL}/im"

def test_get_dialogs_list():
    messages = wd.get_last_messages()
    assert messages is not None