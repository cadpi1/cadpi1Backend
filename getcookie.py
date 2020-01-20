from selenium import webdriver
import time 
import sys

#Get ukc login info from environment variables

def isPageLoaded(driver):
    return driver.execute_script('return document.readyState;')

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.ukclimbing.com/user/")
password = driver.find_element_by_css_selector("#password")
username = driver.find_element_by_css_selector('#email')
submitButton = driver.find_element_by_xpath('//*[@id="main"]/div[1]/form/div[4]/div/button')
submitButton.location_once_scrolled_into_view
password.send_keys("Azerty11$$")    
username.send_keys("Pierre Cadman-Bosse")      
submitButton.click()       

timeout = 0
while not isPageLoaded(driver):
    time.sleep(1)
    timeout = timeout +1
    if(timeout == 10):
        driver.quit()
        exit()

cookies = driver.get_cookies()
ukcCookie = [cookie for cookie in cookies if cookie['name']=='ukcsid'][0]
sys.stdout.write(ukcCookie['value'])
driver.quit()