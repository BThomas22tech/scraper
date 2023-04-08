from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#specify driver path
DRIVER_PATH = 'Users\muckr\OneDrive\Documents\chromedriver'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://indeed.com')

#search software development
search_job = driver.find_element(By.XPATH,'//*[@id="text-input-what"]')
search_job.send_keys(['software development'])
location = driver.find_element(By.ID, 'text-input-where')
location.send_keys(Keys.CONTROL + 'a')
location.send_keys(Keys.DELETE)
location.send_keys(['Nashville'])
#set display limit of 30 results per page
# display_limit = driver.find_element_by_xpath('//select[@id="limit"]//option[@value="30"]')
# display_limit.click()
#sort by date
# //*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/div[3]/div/div/div[1]/span[2]/a
# sort_option = driver.find_element_by_xpath('//select[@id="sort"]//option[@value="date"]')
# sort_option.click()

search_button = driver.find_element(By.XPATH,'//*[@id="jobsearch"]/button')
search_button.click()