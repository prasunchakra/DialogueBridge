from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = Chrome(executable_path='F:\TestingWorld\SeleniumPython\chromedriver.exe')
driver.get('http://www.thetestingworld.com')
driver.maximize_window()

# Select all Ctrl+A
act = ActionChains(driver)
act.send_keys(Keys.CONTROL).send_keys("a").perform()

# Left Click
act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()
# Right Click
act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# Press TAB
driver.find_element_by_name('username')
act = ActionChains(driver)
act.send_keys(Keys.TAB).perform()

# Mouse Hover
act.move_to_element(driver.find_element_by_xpath("//a[text()='Login']")).perform()