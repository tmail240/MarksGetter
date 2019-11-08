from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
import os
import xlrd
import xlwt
from xlutils.copy import copy
import pandas as pd
from datetime import date

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


def isValidUrl(driver,url):
    driver.get(url)
    wait = WebDriverWait(driver,600)
    time.sleep(5)
    flag = True
    try:
        if len(driver.find_elements_by_class_name("leaderboard-hackername"))==0:
            flag = False
    except:
        flag = False
    return flag


def writeSimpleRecord(student_score,test_name,max_score,section):
    name = "hck.xlsx"
    sheet = pd.read_excel(name)
    if str(test_name+"_MM") not in sheet.columns:
        sheet[test_name+"_MM"] = max_score
    if str(test_name+"_MO") not in sheet.columns:
        sheet[test_name+"_MO"] = 0.00
    for student in student_score:
        sheet.loc[ sheet["HackerRank Id"]==student.lower() ,test_name+"_MO"] = student_score[student]
    sheet.to_excel("temp.xlsx",index=False)
    os.remove(name)
    os.rename("temp.xlsx",name)
    print("Record Written Successfully")