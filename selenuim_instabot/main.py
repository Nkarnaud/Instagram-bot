from selenium import webdriver
from home_page import HomePage

browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.get_login_page()
login_page.login("Your username", "Your Password")

browser.close()
