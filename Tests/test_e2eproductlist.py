import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.checkoutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from Utilities.Baseclass import Baseclass


class TestOne(Baseclass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR,("a[class*='btn-primary']")).click()
        #self.driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()
        # self.driver.find_element(By.ID, "country").send_keys("ind")

        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")
        #time.sleep(15)
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)


















































'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
#here the browser invokation code is reusable hence can be placed in fixture
#conftest is a file is a centralized place to keep all fixtures
#As the browser invokation code is elsewhere the driver object throws error in this class bcoz its not defined when we return driver object from that class then we cannot use yield and return together
#Yield will have browser closing statement and cannot be used with return hence need to follow another method
#now if we have multiple classes and test cases inside the file then we need to use browser invokation fixture statement everywhere before the class to optimize it just create a separate class with the fixture and inherit here in every class
#@pytest.mark.usefixtures("invokeBrowsersetup")
from PageObjects.HomePage import Homepage
from PageObjects.checkoutPage import checkoutpage
from Utilities.Baseclass import Baseclass
from PageObjects.confirmPage import confirmPage


class Test2(Baseclass):
    def test_e2e(self):
        HomePage=Homepage(self.driver)#Creating object of class Homepage and sends driver as agrument because the constructor in Hompeage accepts driver argument
        CheckOut=HomePage.shopItems()#accessing methods from object
        #self.driver.find_element(By.CSS_SELECTOR,"a[href='/angularpractice/shop']").click()->
        #CheckOut=checkoutpage(self.driver)
        #products=CheckOut.get_products()
        cards = CheckOut.getCardTitle()
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        i=-1
        for card in cards:
            i=i+1
            #prodname = product.find_element(By.XPATH, "div/h4/a").text
            cardText = card.text
            #prod=CheckOut.get_prodname().text
            if cardText == "Blackberry":
                CheckOut.get_footer()[i].click()
                #product.find_element(By.XPATH, "div/button").click()
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()#checkout button
        #checkOut=checkoutpage(self.driver)
        CheckOut.get_first_checkout().click()
        confirm_Page=CheckOut.get_second_checkout()
        time.sleep(2)
        # driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']")
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()#next page checkout button
        #self.driver.find_element(By.ID, "country").send_keys("ind")
        #confirm_Page= confirmPage(self.driver)
        confirm_Page.confirm_page().send_keys("ind")
        #wait = WebDriverWait(self.driver, 10)
        #to check for locator presence we can have this code in baseclass and call from there
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirm_Page.get_country().click()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirm_Page.get_chkbox().click()
        # xpath->//input[@class='btn btn-success btn-lg']
        # xpath->//input[@type='submit']
        # CSS->input[type='submit']
        # CSS->[type='submit']
        confirm_Page.submit.click()
        #self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()  # by removing tag name in CSS if its uniquely identified
        successtext = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
        assert "Success! Thank you!" in successtext
    '''

