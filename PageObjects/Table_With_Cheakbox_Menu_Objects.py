from selenium.webdriver.common.by import By


class Table_With_Cheakbox_Objects:
    Table_With_Cheakbox = (By.XPATH, "//a[normalize-space()='Table With Checkbox']")
    Cat = (By.XPATH, '//*[@id="post-body-3107268830657760720"]/div[1]/table/tbody/tr[1]/td[1]/input')
    Dog = (By.XPATH, '//*[@id="post-body-3107268830657760720"]/div[1]/table/tbody/tr[2]/td[2]/input')
    Cow = (By.XPATH, '//*[@id="post-body-3107268830657760720"]/div[1]/table/tbody/tr[3]/td[1]/input')
    Lion = (By.XPATH, '//*[@id="post-body-3107268830657760720"]/div[1]/table/tbody/tr[4]/td[2]/input')
    Tiger = (By.XPATH, '//*[@id="post-body-3107268830657760720"]/div[1]/table/tbody/tr[5]/td[1]/input')

    def __init__(self, driver):
        self.driver = driver

    def table_with_cheakbox(self):
        self.driver.find_element(*Table_With_Cheakbox_Objects.Table_With_Cheakbox).click()

    def cat(self):
        self.driver.find_element(*Table_With_Cheakbox_Objects.Cat).click()

    def dog(self):
        self.driver.find_element(*Table_With_Cheakbox_Objects.Dog).click()

    def cow(self):
        self.driver.find_element(*Table_With_Cheakbox_Objects.Cow).click()

    def lion(self):
        self.driver.find_element(*Table_With_Cheakbox_Objects.Lion).click()

    def tiger(self):
        self.driver.find_element(*Table_With_Cheakbox_Objects.Tiger).click()
