


import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as Wait 






USER = "standard_user"
PASSWORD="secret_sauce"

def main():

    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option = webdriver.ChromeOptions("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome (service=service,options=option)
    driver.get("https://saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys(USER)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
   
    button = driver.find_element(By.ID, "login-button")
    button.click()

    #COMPRAS

    driver.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt" ).click()
    driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)" ).click()

    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a" ).click()
    

    driver.find_element(By.ID,"checkout" ).click()
    driver.find_element(By.ID, "first-name").send_keys("Toni")
    driver.find_element(By.ID, "last-name").send_keys("Maroto")
    driver.find_element(By.ID, "postal-code").send_keys('46900')
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    time.sleep(10) 




    driver.quit()



if __name__== "__main__":
    main()