from selenium.webdriver.common.by import By

from PageObjects.confirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_css_selector(".card-title a")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage























'''
from selenium.webdriver.common.by import By

from PageObjects.confirmPage import confirmPage


class checkoutpage:
    def __init__(self,driver):
        self.driver=driver
    cards=(By.XPATH, "//div[@class='card h-100']")
    #prodname= products.find_element(By.XPATH, "div/h4/a").text
    prodname=(By.XPATH, "div/h4/a")
    footer=(By.XPATH, "div/button")
    #product.find_element(By.XPATH, "div/button").click()
    checkout1=(By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout2=(By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*checkoutpage.cards)

    def get_prodname(self):
        return self.driver.find_element(*checkoutpage.prodname)

    def get_footer(self):
        return self.driver.find_element(*checkoutpage.footer)

    def get_first_checkout(self):
        return self.driver.find_element(*checkoutpage.checkout1)

    def get_second_checkout(self):
        self.driver.find_element(*checkoutpage.checkout2).click()
        confirm_Page = confirmPage(self.driver)
        return confirm_Page
    '''



