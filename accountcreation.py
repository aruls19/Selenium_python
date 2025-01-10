import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as x

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver,50)


data = {}
with open("D:/Training/pythonProject/Assignment2/input_file.txt", 'r') as file:
    for line in file:
        key, value = line.strip().split('=', 1)
        data[key.strip()] = value.strip()
    #print(data)

def login(driver,username,password):
    driver.get("https://login.salesforce.com/")
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"Login").click()

   # WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//div/h2[text()='Welcome, Arul']")))

# sales_xpath="//a/span[text()='Sales']"
# driver.find_element(By.XPATH,sales_xpath).click()

#create lead and convert into Account
def usecase1(driver,data):
    wait.until(EC.presence_of_element_located((By.XPATH,x.lead_pagetitle)))

    driver.find_element(By.XPATH,x.lead_new_button).click()

    wait.until(EC.presence_of_element_located((By.XPATH,x.new_lead_window)))
    driver.find_element(By.XPATH,x.lead_firstname).send_keys(data['lead_firstname_value'])
    driver.find_element(By.XPATH,x.lead_lastname).send_keys(data['lead_lastname_value'])
    driver.find_element(By.XPATH,x.lead_companyname).send_keys(data['lead_companyname_value'])
    driver.find_element(By.XPATH,x.lead_savebutton).click()

    #lead to account convertion
    wait.until(EC.presence_of_element_located((By.XPATH,x.leadpage_convertbutton)))
    driver.find_element(By.XPATH,x.leadpage_convertbutton).click()
    wait.until(EC.presence_of_element_located((By.XPATH,x.lead_convertwindow)))
    time.sleep(5)
    driver.find_element(By.XPATH,x.leadtoaccount_convert_button).click()

#Attach the contacts and Opportunity to created account
def usecase2(driver,data):
    account_name_link_xpath=x.account_name_link.replace("OLD",data['lead_companyname_value'])
    wait.until(EC.presence_of_element_located((By.XPATH,account_name_link_xpath)))
    driver.find_element(By.XPATH,account_name_link_xpath).click()
    wait.until(EC.presence_of_element_located((By.XPATH,x.account_pagetitle)))

    driver.find_element(By.XPATH,x.new_contact_button).click()
    wait.until(EC.presence_of_element_located((By.XPATH,x.new_contact_window)))
    time.sleep(5)
    driver.find_element(By.XPATH,x.contact_lastname).send_keys(data['contact_lastname_value'])
    driver.find_element(By.XPATH,x.contact_savebutton).click()

    driver.find_element(By.XPATH,x.new_opportunity_button).click()
    wait.until(EC.presence_of_element_located((By.XPATH,x.new_opportunity_window)))
    time.sleep(5)
    driver.find_element(By.XPATH,x.new_opportunity_savebutton).click()

def main_assignment():
    login(driver, data['username'], data['password'])
    usecase1(driver, data)
    usecase2(driver, data)

    driver.quit()
    print("completed")

main_assignment()





