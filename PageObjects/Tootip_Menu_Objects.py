from selenium.webdriver.common.by import By


class Tooltip_Objects:
    Tooltip = (By.XPATH, "//a[normalize-space()='Tooltip']")
    Name = (By.XPATH, "//input[@id='tooltip-1']")
    Surname = (By.XPATH, "//input[@id='sname']")
    Address = (By.XPATH, "//input[@id='yaddress']")

    def __init__(self, driver):
        self.driver = driver

    def tooltip(self):
        self.driver.find_element(*Tooltip_Objects.Tooltip).click()

    def name(self, data):
        self.driver.find_element(*Tooltip_Objects.Name).clear()
        self.driver.find_element(*Tooltip_Objects.Name).send_keys(data)

    def surname(self, data):
        self.driver.find_element(*Tooltip_Objects.Surname).clear()
        self.driver.find_element(*Tooltip_Objects.Surname).send_keys(data)

    def address(self, data):
        self.driver.find_element(*Tooltip_Objects.Address).clear()
        self.driver.find_element(*Tooltip_Objects.Address).send_keys(data)
