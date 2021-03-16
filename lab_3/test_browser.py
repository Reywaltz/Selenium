from main import wd, URL


def test_site_available():
    wd.driver.get(URL)
    form = wd.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form')
    assert form is not None
def test_empty_field():
    wd.driver.get(URL)
    err_label = wd.empty_press()
    assert err_label == 'Заполните обе дроби'

def test_negative_fraction():
    wd.driver.get(URL)
    err_label = wd.decimal_to_fraction()
    assert err_label == 'Введите число'

def test_simple_to_mixed():
    wd.driver.get(URL)
    res = wd.simple_to_mixed()
    assert res != None

def test_percentage_to_fraction():
    wd.driver.get(URL)
    res = wd.percentage_to_fraction()
    assert res != None