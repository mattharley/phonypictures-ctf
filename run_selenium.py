import time

from selenium import webdriver

def login_as_boss():
    while 1:
        try:
            with WebDriver() as driver:
                driver.get("http://172.17.42.1:5000")

                username = driver.find_element_by_id('username')
                password = driver.find_element_by_id('password')

                username.send_keys('bigboss')
                password.send_keys('b!gb0ss')

                submit = driver.find_element_by_id('submit')

                submit.click()
        except:
            pass
    time.sleep(10)

if __name__ == '__main__':
    login_as_boss()

class WebDriver():
    def __init__(self):
        self.driver = None
    def __enter__(self):
        self.driver = webdriver.Firefox()
        return self.driver
    def __exit__(self, type, value, traceback):
        self.driver.quit()