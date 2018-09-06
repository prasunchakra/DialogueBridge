from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    driver = Chrome(executable_path='F:\TestingWorld\SeleniumPython\chromedriver.exe')
    driver.get('http://www.thetestingworld.com/testings/')
    driver.maximize_window()

    yield
    driver.close()
def test_varify_registration(environment_setup):
    driver.find_element_by_name("fld_username").send_keys("pharmaeasy")
    driver.find_element_by_name("fld_email").send_keys("care@pharmaeasy.com")
    driver.find_element_by_xpath("//input[@name='fld_password']").send_keys("CRPK30")
    driver.find_element_by_xpath("//input[@name='fld_cpassword']").send_keys("CRPK30")
    driver.find_element_by_xpath("//input[@value='home']").click()
    driver.find_element_by_xpath("//input[@name='terms']").click()
    obj = Select(driver.find_element_by_name('sex'))
    obj.select_by_index(2)
    obj = Select(driver.find_element_by_name('country'))
    obj.select_by_value("2")

    assert driver.current_url=="http://www.thetestingworld.com/testings/register.php"
