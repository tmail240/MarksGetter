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


student_scoreboard = dict()
# new_driver = webdriver.Chrome("chromedriver.exe")
# login(new_driver)

# max_score = getMaxScore(driver)

href = driver.find_element_by_class_name("w_challenges_side_list").find_element_by_class_name("backbone").get_attribute("href")

driver.get(href)
time.sleep(7)

t_leaders = driver.find_element_by_id("leaders")
leaders = t_leaders.find_elements_by_class_name("span-flex-4")
for j in range(len(leaders)):
    leader = leaders[j].find_element_by_class_name("leaderboard-hackername")
    leader_name = leader.get_attribute("data-attr1")
    leader_score = t_leaders.find_elements_by_class_name("span-flex-3")[2*j].find_element_by_tag_name("p").text
    student_scoreboard[leader_name] = student_scoreboard.get(leader_name,0)+float(leader_score)


wait = WebDriverWait(driver, 1200)
time.sleep(3)

logout(driver)
driver.close()