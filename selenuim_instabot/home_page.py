from insta_login import LoginPage


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def get_login_page(self):
        return LoginPage(self.browser)
