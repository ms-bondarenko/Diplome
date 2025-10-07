from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class AuthPage:
    def __init__(self, driver)->None:
        self.__driver = driver
        self.__url = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D%26jiraInviteLink%3D"

    def go(self):
        self. __driver.get(self.__url)

    def login_as(self, email: str,password: str ):
        self.__driver.find_element(By.CSS_SELECTOR, "#username-uid1").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    def get_current_url(self):
        WebDriverWait(self.__driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "QEGH0t6lsxm4C9"))
        )
        return self.__driver.current_url


