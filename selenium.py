from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login_as_boss():
    driver = webdriver.Firefox()
    driver.get("127.0.0.1:5000")

    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')

    username.send_keys("bigboss")
    password.send_keys('bigboss')

    submit = driver.find_element_by_id('submit')

    submit.click()

if __name__ == '__main__':
    login_as_boss()