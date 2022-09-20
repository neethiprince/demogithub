class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver



'''
from selenium.webdriver.common.by import By


class confirmPage:
    def __init__(self,driver):
        self.driver=driver
    details=(By.ID, "country")
    #.send_keys("ind"))
    country=(By.LINK_TEXT, "India")
    chkbox=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    sub=(By.CSS_SELECTOR,"[type='submit']")
    def confirm_page(self):
        return self.driver.find_element(*confirmPage.details)
    #By.XPATH, "//button[@class='btn btn-success']")

    def get_country(self):
        return self.driver.find_element(*confirmPage.country)

    def get_chkbox(self):
        return self.driver.find_element(*confirmPage.chkbox)

    def submit(self):
        return self.driver.find_element(*confirmPage.sub)'''
