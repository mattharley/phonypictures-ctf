import logging
import time

from selenium import webdriver

logger = logging.getLogger(__name__)
logformat = "%(asctime)s: %(message)s"
logging.basicConfig(level=logging.DEBUG,format=logformat)

class WebDriver():
    def __init__(self):
        self.driver = None
    def __enter__(self):
        logger.info('Fetching webdriver...')
        self.driver = webdriver.Firefox()
        logger.info('Done.')
        return self.driver
    def __exit__(self, type, value, traceback):
        self.driver.quit()

def login_as_boss():
    while 1:
        try:
            with WebDriver() as driver:
                url = "http://172.17.42.1:5000"
                logger.info("Getting {}".format(url))
                driver.get(url)

                username = driver.find_element_by_id('username')
                password = driver.find_element_by_id('password')

                username.send_keys('bigboss')
                password.send_keys('b!gb0ss')

                submit = driver.find_element_by_id('submit')

                logger.info("Submit!")
                submit.click()
        except Exception as e:
            logger.exception(e)
    logger.info("Sleepy time...")
    time.sleep(10)

if __name__ == '__main__':
    logger.info('Starting up...')
    login_as_boss()