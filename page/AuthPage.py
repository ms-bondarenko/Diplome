from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.core import driver


class AuthPage:
    def __init__(self, driver)->None:
        self._driver = driver
        self._url = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D%26jiraInviteLink%3D"

    def go(self):
        self._driver.get(self._url)