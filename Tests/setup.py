import pytest
from selenium import webdriver

global url
url = "https://www.toptal.com/"

class SetUp:

    @pytest.fixture()
    def browser(self):
        driver = webdriver.Chrome(executable_path="C:/Users/mm195/Desktop/YMLILGEE/Programs/Gecko Driver/chromedriver_win32/chromedriver.exe")
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        # Return the driver object at the end of setup
        yield driver

        # For cleanup, quit the driver
        driver.quit()