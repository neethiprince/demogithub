
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from PageObjects.HomePage import HomePage
from Utilities.Baseclass import Baseclass


class TestHomePage(Baseclass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        log.info("email is " + getData["email"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckBox().click()
        log.info("gender is " + getData["gender"])
        self.selectbytext(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(
        params=HomePageData.getTestData("Testcase4"))  # with static method w/o using self and without creating object
    def getData(self, request):
        return request.param


'''
      @pytest.fixture(params=HomePageData.test_HomePage_data)#with non static method with using self and creating object
    def getData(self, request):
        return request.param
'''
'''
import time
from selenium import webdriver  # class webdriver imported from selenium package
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from Utilities.Baseclass import Baseclass


class testhomepage(Baseclass):

    def test_Form(self):
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        HomePage=Homepage(self.driver)
        HomePage.getName().send_keys("Neethi Prince")
        # ID,Xpath,CSS selector,Class name,name,linktext
        # xpath and CSS can be constructed for any element on the page unlike name,id,linktext
        #self.driver.find_element(By.NAME, "name").send_keys("Neethi Prince")
        # driver.find_element(By.CSS_SELECTOR,"input[name='name']")->By CSS
        # driver.find_element(By.XPATH,"//input[@name='name']")
        # for cssselector -> tagname[attribute='value'] or #id or .classname
        # for Xpath //input[@type='text'] in "Two way data binding ex" edit box ->3 elements matching-> now to select 3 matched element use syntax (//input[@type='text'])[3]
        # for Xpath //input[@class='ng-pristine ng-valid ng-touched'] in "Two way data binding ex" edit box ->1 element matching

        # driver.find_element(By.NAME,"email").send_keys("Neethiprince@techment.com")
        # driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("Neethiprince@techment.com")
        # self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Neethiprince@techment.com")
        HomePage.getemail().send_keys("Neethiprince@techment.com")
        time.sleep(2)
        #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("123")
        HomePage.getpassword().send_keys("123")
        time.sleep(2)
        HomePage.getCheckBox().click()
        #self.driver.find_element(By.ID, "exampleCheck1").click()
        time.sleep(2)
        # for xpath -> //tagname[@attribute='value']
        # Static dropdown->whenever we see select tag in inspect then we can use select class to handle it and the dropdown is static dropdown
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        self.selectbytext(HomePage.getGender(),"Female")
        #sel= Select(HomePage.getgender())
        #sel.select_by_index(0)
        #time.sleep(2)
        #sel.select_by_visible_text("Female")
        #dropdown.select_by_index(0)
        time.sleep(2)
        # dropdown.select_by_value("")#value can be used if value is defined in option tag in our case its not defined hence we can locate by value
        #dropdown.select_by_visible_text("Female")
        # driver.find_element(By.XPATH , "//option[@value='Female']")
        HomePage.submitform().click()
        alertText=HomePage.getsuccessmessage().text
        driver.find_element(By.CSS_SELECTOR, "label[for='inlineRadio2']").click()
        # driver.find_element(By.ID,"exampleFormControlSelect1").send_keys("123")
        # driver.find_element(By.ID,"exampleInputPassword1").send_keys("123")
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("12")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        msg = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(msg)
        assert "Success" in msg

        driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
        # we can add locators validator "SelectorsHub" to check if the xpath and CSS syntax is correct or how many unique locators with that name is present.
        '''