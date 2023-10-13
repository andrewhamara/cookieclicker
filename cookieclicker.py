###################################################################
                                                                  #
from selenium import webdriver                                    #
from selenium.webdriver.chrome.service import Service             #
from selenium.webdriver.support.ui import WebDriverWait           #
from selenium.webdriver.support import expected_conditions as EC  #
from selenium.webdriver.common.by import By                       #
from selenium.webdriver.common.keys import Keys                   #
                                                                  #
_service = Service()                                              #
_options = webdriver.ChromeOptions()                              #
_options.add_argument("--window-size=1920,1080")                  #
driver = webdriver.Chrome(service=_service, options=_options)     #
                                                                  #
###################################################################


###################################################################
                                                                  #
import time                                                       #
import logging                                                    #
import sys                                                        #
                                                                  #
# How critical can cookies really be                              #
logging.basicConfig(level=logging.CRITICAL)                       #
                                                                  #
###################################################################






def main():
    driver.get('https://orteil.dashnet.org/cookieclicker/')

    englishButton = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]'))
    )

    englishButton.click()

    cookie = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'bigCookie'))
    )

    finger = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[19]/div[3]/div[6]/div[2]'))
    )

    grandma = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[19]/div[3]/div[6]/div[3]'))
    )

    for _ in range (100):
        driver.execute_script("arguments[0].click();", cookie)
        time.sleep(0.1)
        driver.execute_script("arguments[0].click();", finger)
        time.sleep(0.1)
        driver.execute_script("arguments[0].click();", grandma)
        time.sleep(0.1)


    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
