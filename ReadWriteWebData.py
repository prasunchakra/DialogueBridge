from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time

# Open Browser
driver = Chrome(executable_path='F:\TestingWorld\SeleniumPython\chromedriver.exe')


# Enter URL
driver.get('http://www.thetestingworld.com/testings/')

print (driver.title)
print (driver.current_url)
HTML= driver.page_source
# Maximize Window
driver.maximize_window()

# Enter Data to Text Boxes
driver.find_element_by_name("fld_username").send_keys("pharmaeasy")
driver.find_element_by_name("fld_email").send_keys("care@pharmaeasy.com")
driver.find_element_by_xpath("//input[@name='fld_password']").send_keys("CRPK30")
driver.find_element_by_xpath("//input[@name='fld_cpassword']").send_keys("CRPK30")
# ReEnter Data to Text Boxes
driver.find_element_by_xpath("//input[@name='fld_username']").clear() # without clear send_keys append the text
driver.find_element_by_xpath("//input[@name='fld_username']").send_keys("PharmaEasy")
# Work on Radio Button
driver.find_element_by_xpath("//input[@value='home']").click()
# Work on Check Box
driver.find_element_by_xpath("//input[@name='terms']").click()
# Work on Links
#driver.find_elements_by_link_text("Read Detail")[0].click()

# Work on Drop Down or list
obj = Select(driver.find_element_by_name('sex'))
obj.select_by_index(2)
obj = Select(driver.find_element_by_name('country'))
obj.select_by_value("2")
obj = Select(driver.find_element_by_name('country'))

# Close Browser
time.sleep(3)
driver.close()
