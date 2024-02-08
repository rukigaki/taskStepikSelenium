from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_btn_wishlist(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn-wishlist")
