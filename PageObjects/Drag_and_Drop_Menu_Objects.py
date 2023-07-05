from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Drag_and_Drop_Objects:
    Drag_and_Drop = (By.XPATH, "//a[normalize-space()='Drag and Drop']")
    S = (By.XPATH, '//*[@id="dragdiv"]')
    T = (By.XPATH, "//div[@id='dropdiv']")
    Resize = (By.XPATH, '//*[@id="resizable"]/div[3]')

    def __init__(self, driver):
        self.driver = driver

    def drag_and_drop(self):
        self.driver.find_element(*Drag_and_Drop_Objects.Drag_and_Drop).click()

    def drag_and_drop1(self):
        action = ActionChains(self.driver)
        Source = self.driver.find_element(*Drag_and_Drop_Objects.S)
        Target = self.driver.find_element(*Drag_and_Drop_Objects.T)
        action.drag_and_drop(Source, Target).perform()

    def resize(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*Drag_and_Drop_Objects.Resize)
        action.drag_and_drop_by_offset(element, 400, 8).perform()