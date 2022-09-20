import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def invokeBrowsersetup(request):#request is an instance by default declared while declaring fixture
    #service_obj = Service("C:\\Users\\Techment Technology\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
    # this is the chrome service because from chrome service we have imported service and here we are creating an object of the service
    #driver = webdriver.Chrome(service=service_obj)
    browser_name = request.config.getoption("browser_name")#retrieve the value present in key value
    if browser_name=="chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\Techment Technology\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

    elif browser_name=="edge":
        #service_obj = Service("C:\\Users\\Techment Technology\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        #driver = webdriver.Edge(service=service_obj)
        #driver = webdriver.Chrome(
        driver = webdriver.Edge(executable_path="C:\\Users\\Techment Technology\\Downloads\\edgedriver_win64\\msedgedriver.exe")
    driver.implicitly_wait(4)
    #driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver=driver#we are declaring our local fixture driver to the class driver(request.cls.driver)
    yield
    driver.close()

    '''
    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
    '''

