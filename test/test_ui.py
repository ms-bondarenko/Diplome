from ..page.AuthPage import AuthPage

def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("vampnnight674@gmail.com","HellkatM18/")

    assert auth_page.get_current_url().endswith("vampnnight674/boards")


