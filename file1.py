from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
from mods import login, logout

driver = webdriver.Chrome('chromedriver.exe')
driver.minimize_window()

login(driver)

# marks fetching link

url = "https://www.hackerrank.com/contests/"+ input("Enter Contest Name") +"/challenges"



driver.get(url)

wait = WebDriverWait(driver, 1200)
time.sleep(3)

logout(driver)
driver.close()