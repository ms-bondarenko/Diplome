from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ..page.AuthPage import AuthPage
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options

def test_first():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)

    auth_page = AuthPage(browser)
    auth_page.go()

    sleep(5)
    browser.quit()


