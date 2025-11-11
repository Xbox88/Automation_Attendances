import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def submit_attendance(attendances_code,tp_number,password):
    wd = webdriver.Chrome()

    wd.get("https://apspace.apu.edu.my/login")

    time.sleep(3)
    wd.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[1]/ion-col[2]/ion-button").click()

    time.sleep(3)
    wd.find_element(By.CSS_SELECTOR,"body > app-root > ion-app > ion-router-outlet > app-login > ion-content > div > section.login > div > ion-grid > ion-row.login-hidden-section.md.hydrated > ion-col:nth-child(1) > form > div > div > div:nth-child(1) > ion-input > input").send_keys(tp_number)
    wd.find_element(By.CSS_SELECTOR,"body > app-root > ion-app > ion-router-outlet > app-login > ion-content > div > section.login > div > ion-grid > ion-row.login-hidden-section.md.hydrated > ion-col:nth-child(1) > form > div > div > div:nth-child(2) > div > ion-input > input").send_keys(password)

    time.sleep(1)
    wd.find_element(By.CSS_SELECTOR,"body > app-root > ion-app > ion-router-outlet > app-login > ion-content > div > section.login > div > ion-grid > ion-row.login-hidden-section.md.hydrated > ion-col:nth-child(1) > form > div > div > div.login-button-container > ion-button").click()

    time.sleep(3)
    wd.find_element(By.CSS_SELECTOR,"#tab-button-attendance > ion-label").click()
    time.sleep(1)
    wd.find_element(By.CSS_SELECTOR,"body > app-root > ion-app > ion-router-outlet > app-tabs > ion-content > ion-tabs > div > ion-router-outlet > app-attendance > ion-content > div > ion-row > ion-col:nth-child(1) > ion-card > ion-card-content > ion-button").click()
    time.sleep(1)
    wd.find_element(By.CSS_SELECTOR,"body > app-root > ion-app > ion-router-outlet > app-student > ion-content > ion-row > ion-col > div > input:nth-child(1)").send_keys(str(attendances_code))
    time.sleep(3)

    wd.quit()

