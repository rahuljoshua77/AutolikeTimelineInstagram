import undetected_chromedriver as uc
from time import sleep
uc.install()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random, config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

cwd = os.getcwd()

opts = Options()
opts.headless = True
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])



def open_browser(user, password):
    global browser
    browser = webdriver.Chrome(options=opts, desired_capabilities=dc)
    browser.get("https://www.instagram.com/")
    print(f"[{time.strftime('%d-%m-%y %X')}] Automation Like Timeline Instagram")
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))).send_keys(user)
    print(f"[{time.strftime('%d-%m-%y %X')}] Login...")
    sleep(0.5)
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))).send_keys(password)
    sleep(0.5)
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))).send_keys(Keys.ENTER)
    sleep(5)
    print(f"[{time.strftime('%d-%m-%y %X')}] Logged in...")
    validator = []
    browser.get("https://www.instagram.com/")
    try:
        element = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')))
        browser.execute_script("arguments[0].click();",element)
    except:
        
        pass
    while True:
        browser.get("https://www.instagram.com/")
        for i in range(1, random.randint(1,config.maxLike)):
            try:
                el_article = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(//article/div/div[3]/div/div/div[1])[{i}]')))
                browser.execute_script("arguments[0].scrollIntoView();", el_article)
                el_article = el_article.text
 
                if el_article not in validator:
                    validator.append(el_article)
                    element = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'(//article/div/div[3]/div/div/section[1]/span[1]/button)[{i}]')))
                    browser.execute_script("arguments[0].click();",element)
                    if "\n" in el_article:
                        el_article = el_article.split("\n")
                        el_article = el_article[0]
                    print(f"[{time.strftime('%d-%m-%y %X')}] Status: {el_article} [ SUCCESS LIKE ]")
                else:
                    print(f"[{time.strftime('%d-%m-%y %X')}] Status: {el_article} [ ALREADY LIKE ]")
            except Exception as e:
                pass
            sleep(random.randint(config.minDelayPerLike,config.maxDelayPerLike))

        sleep(random.randint(config.minDelayPerLoop,config.maxDelayPerLoop))

open_browser(config.userName, config.passWord)
