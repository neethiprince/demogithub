from selenium.webdriver.common.by import By

from PageObjects.checkoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)




'''
from selenium.webdriver.common.by import By
#home page is the "https://rahulshettyacademy.com/angularpractice" page.As the shop button is present in home page the home page button will goto homepage class
from PageObjects.checkoutPage import checkoutpage


class Homepage:
    def __init__(self,driver):
        self.driver=driver#sending the actual driver from test case to local class driver
    shop=(By.CSS_SELECTOR,"a[href='/angularpractice/shop']")#tuple with 2 arguments,1st the locator and second the value
    name = (By.NAME, "name")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH , "//option[@value='Female']")
    successmessage = (By.CSS_SELECTOR, "input[type='submit']")
    
    shop = (By.XPATH, "(//input[@type='text'])[3]")
    shop = (By.CSS_SELECTOR, "input[type='submit']")
    shop = (By.CLASS_NAME, "alert-success")
    
    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()#calling the shop object
        CheckOut = checkoutpage(self.driver)
        return CheckOut
        #in the pageobject class driver is not defined here its defined in the e2eproductlist test cases
        #* indicates deserializing touple in propere format
        #CheckOut = checkoutpage(self.driver)
        #return CheckOut

    def getName(self):
        return self.driver.find_element(*Homepage.name).click()

    def getemail(self):
        return self.driver.find_element(*Homepage.email).click()

    def getpassword(self):
        return self.driver.find_element(*Homepage.password).click()

    def getCheckBox(self):
        return self.driver.find_element(*Homepage.check)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def submitForm(self):
        return self.driver.find_element(*Homepage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)
    '''
