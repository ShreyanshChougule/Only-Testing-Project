from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Selectable_Objects:
    Selectable = (By.XPATH, "//a[normalize-space()='Selectable']")

    def __init__(self, driver):
        self.driver = driver

    def selectable(self):
        self.driver.find_element(*Selectable_Objects.Selectable).click()

    def items(self):
        k = 0
        for i in range(1, 8):
            self.driver.find_element(By.XPATH, f'//*[@id="selectable"]/li[{i}]').click()
            self.driver.implicitly_wait(3)
            self.driver.get_screenshot_as_file(f"C:\\Users\\Tejas\\Only Testing Project\\Screenshots\\{k}.png")
            k += 1

    def double_ckick(self):
        action = ActionChains(self.driver)
        alert = Alert(self.driver)
        action.double_click(self.driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")).perform()
        self.driver.implicitly_wait(2)
        tx = alert.text
        alert.accept()
        return tx