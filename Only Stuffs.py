from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Edge()
driver.get()
driver.find_element()
driver.find_element().send_keys()
driver.implicitly_wait()
k = driver.window_handles
driver.switch_to.frame("frame1")
A = ActionChains(driver)
A.click_and_hold(element).move_by_offset(150, 100).Perform()
