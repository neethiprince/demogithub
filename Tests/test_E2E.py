from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
#here the browser invokation code is reusable hence can be placed in fixture
#conftest is a file is a centralized place to keep all fixtures
#As the browser invokation code is elsewhere the driver object throws error in this class bcoz its not defined when we return driver object from that class then we cannot use yield and return together
#Yield will have browser closing statement and cannot be used with return hence need to follow another method
#now if we have multiple classes and test cases inside the file then we need to use browser invokation fixture statement everywhere before the class to optimize it just create a separate class with the fixture and inherit here in every class
#@pytest.mark.usefixtures("invokeBrowsersetup")
from Utilities.Baseclass import Baseclass


class Test1(Baseclass):
    def test_e2e(self):
        #self.driver.implicitly_wait(4)
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        self.driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
        windowcount = self.driver.window_handles

        self.driver.switch_to.window(windowcount[1])  # no clue about the window name hence using window handles
        # username=driver.find_element(By.XPATH,"//div[@class='page-wrapper']//div[@class='container']//div[@class='row']//div[@class='col-md-8']//p[@class='im-para red']//strong").text
        username = self.driver.find_element(By.XPATH,"//div//p[@class='im-para red']//a[contains(@href,'mentor@rahulshettyacademy.com')]").text
        print(username)
        # var=username.split('@')
        password = "learning"
        # xpath->//div//p[@class='im-para red']//a[contains(@href,"mentor@rahulshettyacademy.com")]
        self.driver.close()
        self.driver.switch_to.window(windowcount[0])
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
        # driver.find_element(By.CSS_SELECTOR,"#username").send_keys(var[1])
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        # //span[text()='Admin']
        self.driver.find_element(By.XPATH, "//select//option[@value='stud']").click()
        self.driver.find_element(By.XPATH, "//span[@class='text-white termsText']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-md").click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
        # wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".alert-danger")))
        incorrecttext = self.driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
        print(incorrecttext)
        # print(incorrecttext)
        assert "Incorrect" in incorrecttext

