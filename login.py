from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time

def login(user, passw):
    url = "https://www.hbogola.com/authentication/login"
    page = requests.get(url)
    driver = webdriver.Chrome(
        executable_path=r"./chromedriver.exe")
    driver.get(url)
    time.sleep(2)
    # article = driver.find_elements_by_xpath('//article[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12 archive-box"]')
    boton = driver.find_element_by_id("onetrust-accept-btn-handler")
    boton.send_keys(Keys.TAB)
    boton.send_keys(Keys.TAB)
    boton.send_keys(Keys.ENTER)
    userOk = str(user)
    passwOk = str(passw)

    time.sleep(1)
    user = driver.find_element_by_name("email")
    user.send_keys(str(userOk))
    time.sleep(1)
    passw = driver.find_element_by_name("password")
    passw.send_keys(str(passwOk))
    time.sleep(1)
    submit = driver.find_element_by_xpath('//button[@class="btn btnBlue btnBlock"]')
    submit.send_keys(Keys.ENTER)
    return driver
