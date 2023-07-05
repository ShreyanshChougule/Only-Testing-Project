import time

from selenium.webdriver.common.by import By

from Utilities.Excel_File import Excel_File_Opractions


class IFRAME_Objects:
    IFrame = (By.XPATH, "//a[normalize-space()='iframe1']")
    Cat = (By.XPATH, "//h3[@class='post-title entry-title']")
    Dog = (By.XPATH, "//h3[@class='post-title entry-title']")
    Cow = (By.XPATH, "//h3[@class='post-title entry-title']")
    Lion = (By.XPATH, "//h3[@class='post-title entry-title']")
    Tiger = (By.XPATH, "//h3[@class='post-title entry-title']")

    First_Name = (By.ID, "text1")
    Last_Name = (By.ID, "text2")
    Hidden = (By.ID, "text3")
    Boat = (By.ID, "check3")
    Male = (By.ID, "radio1")
    Car_List = (By.ID, "Carlist")  # Value = "Toyota"
    Multipal_Name = (By.XPATH, '//*[@id="post-body-4292417847084983089"]/div[1]/form[2]/table/tbody/tr/td[1]/select')
    Forward_Button = (By.XPATH, '//*[@id="post-body-4292417847084983089"]/div[1]/form[2]/table/tbody/tr/td[2]/input[1]')
    Show_Me_Confirmation = (By.XPATH, "//h3[@class='post-title entry-title']")

    Town = (By.XPATH, "//input[@id='text1']")
    Country = (By.XPATH, "//input[@id='text2']")

    def __init__(self, driver):
        self.driver = driver

    def iframe1(self):
        self.driver.find_element(*Page_Objects.IFrame).click()
        self.driver.switch_to.frame("frame1")
        self.driver.find_element(*Page_Objects.Cat).click()
        self.driver.find_element(*Page_Objects.Dog).click()
        self.driver.find_element(*Page_Objects.Cow).click()
        self.driver.find_element(*Page_Objects.Lion).click()
        self.driver.find_element(*Page_Objects.Tiger).click()
        self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Only Testing Project\\Screenshots\\Frame-1.png")

        self.driver.switch_to.frame("frame2")