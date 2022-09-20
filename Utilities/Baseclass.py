import time
import inspect
import logging
import pytest
#as the Baseclass is aware of this fixture we can inherit this class in child class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects import HomePage


@pytest.mark.usefixtures("invokeBrowsersetup")
class Baseclass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger#pass is used just to pass and no operation performed

    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 10)
        # to check for locator presence we can have this code in baseclass and call from there
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectbytext(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)