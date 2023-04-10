from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv
# specify driver path
DRIVER_PATH = 'Users\muckr\OneDrive\Documents\chromedriver'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://indeed.com')


search_job = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
search_job.send_keys(['software development'])
location = driver.find_element(By.ID, 'text-input-where')
location.send_keys(Keys.CONTROL + 'a')
location.send_keys(Keys.DELETE)
location.send_keys(['Nashville'])

search_button = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button')
search_button.click()

jobs = []
titles = []
companies = []
salaries = []
wait = WebDriverWait(driver, 10)


soup = BeautifulSoup(driver.page_source, 'html.parser')
job_cards = wait.until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "jobCard_mainContent")))

for card in job_cards:
        try:
            title = card.find_element(
                By.CSS_SELECTOR, '.jcs-JobTitle').text
            titles.append(title)
        except:
            title = "None"
            titles.append(title)

        try:
            company = card.find_element(By.CLASS_NAME, "companyInfo ").text
            companies.append(company)
        except:
            company = "None"
            companies.append(company)
        try:
            salary = card.find_element(By.CLASS_NAME, "salaryOnly").text
            salaries.append(salary)
        except:
            salary = "None"
            salaries.append(salary)
        job = {'title': title, 'company': company, 'salary': salary}
        jobs.append(job)
# for page in range(1,4):
#     try:
#         next_button = driver.find_element(
#             By.CSS_SELECTOR, 'a[data-testid="pagination-page-{}"]'.format(page+2))
#         next_url = next_button.get_attribute("href")
#         driver.get(next_url)
#         job_cards = wait.until(EC.presence_of_all_elements_located(
#             (By.CLASS_NAME, "jobCard_mainContent")))
#     except:
#         "None"
with open('jobdata.csv','a',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Company', 'Salary'])
    for job in jobs:
        writer.writerow([job['title'],job['company'],job['salary']+ '\n'])
        # print(f'Title: {title}\nCompany: {company}\nSalary: {salary}\n')

