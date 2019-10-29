from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

def login(driver):
    driver.get("https://hackerrank.com/auth/login")
    wait = WebDriverWait(driver, 600) 
    email = driver.find_element_by_id("input-1")
    email.send_keys("abc@example.com")
    password = driver.find_element_by_id("input-2")
    password.send_keys("password")
    loginBtn  = driver.find_element_by_class_name("auth-button")
    loginBtn.click()
    time.sleep(10)


def logout(driver):
    driver.get("https://www.hackerrank.com/dashboard")
    logoutDropdown = driver.find_element_by_class_name("dropdown-auth")
    logoutDropdown.click()
    time.sleep(2)
    logoutBtn = driver.find_element_by_class_name("logout-button")
    logoutBtn.click()
