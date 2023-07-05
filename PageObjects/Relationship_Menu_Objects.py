from selenium.webdriver.common.by import By


class Relationship_Objects:
    Relationship = (By.XPATH, "//a[normalize-space()='Relationship']")
    Grand_Parent1 = (By.XPATH, "//input[@id='gparent_1']")
    Parent1 = (By.XPATH, "//input[@id='parent_1']")
    Child1 = (By.XPATH, "//input[@id='child_1']")
    Grand_Parent2 = (By.XPATH, "//input[@id='gparent_2']")
    Parent2 = (By.XPATH, "//input[@id='parent_2']")
    Child2 = (By.XPATH, "//input[@id='child_2']")
    Home = (By.XPATH, "//a[@class='home-link']")

    def __init__(self, driver):
        self.driver = driver

    def relationship(self):
        self.driver.find_element(*Relationship_Objects.Relationship).click()

    def grand_parent1(self, data):
        self.driver.find_element(*Relationship_Objects.Grand_Parent1).clear()
        self.driver.find_element(*Relationship_Objects.Grand_Parent1).send_keys(data)

    def parent1(self, data):
        self.driver.find_element(*Relationship_Objects.Parent1).clear()
        self.driver.find_element(*Relationship_Objects.Parent1).send_keys(data)

    def child1(self, data):
        self.driver.find_element(*Relationship_Objects.Child1).clear()
        self.driver.find_element(*Relationship_Objects.Child1).send_keys(data)

    def grand_parent2(self, data):
        self.driver.find_element(*Relationship_Objects.Grand_Parent2).clear()
        self.driver.find_element(*Relationship_Objects.Grand_Parent2).send_keys(data)

    def parent2(self, data):
        self.driver.find_element(*Relationship_Objects.Parent2).clear()
        self.driver.find_element(*Relationship_Objects.Parent2).send_keys(data)

    def child2(self, data):
        self.driver.find_element(*Relationship_Objects.Child2).clear()
        self.driver.find_element(*Relationship_Objects.Child2).send_keys(data)

    def status(self, File_Name):
        self.driver.get_screenshot_as_file(f"C:\\Users\\Tejas\\Only Testing Project\\Screenshots\\{File_Name}.png")
        self.driver.implicitly_wait(2)
        self.driver.find_element(*Relationship_Objects.Home).click()
