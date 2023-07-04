from curses import window
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--lang=en')
options.add_argument('log-level=3')
options.add_argument('--mute-audio')
options.add_argument("--enable-webgl-draft-extensions")
options.add_argument("--ignore-gpu-blocklist")
options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
options.add_argument('--no-sandbox')
options.add_argument('--autoplay-policy=no-user-gesture-required')
options.add_argument('--start-maximized')    
options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-blink-features")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--enable-javascript")
options.add_argument("--disable-notifications")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--enable-popup-blocking")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", [
    "enable-logging",
    "enable-automation",
    "ignore-certificate-errors",
    "safebrowsing-disable-download-protection",
    "safebrowsing-disable-auto-update",
    "disable-client-side-phishing-detection"])
options.add_argument("disable-infobars")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)



# chrome_executable = Service(executable_path='/home/hp/Documents/nency/seleniumpro/chromedriver')
# driver=webdriver.Chrome(service=chrome_executable)
driver.get('https://www.amazon.in/')
driver.maximize_window()
# action=ActionChains(driver)
time.sleep(2)
# #-------print title----------
# print(driver.title)

# #-------search field---------     
# search=driver.find_element(By.NAME,"field-keywords")
# search.send_keys('products')
# search.send_keys(Keys.ENTER)

# #-------hover on element---------

# hoverele=driver.find_element(By.CSS_SELECTOR,"a#icp-nav-flyout")
# action.move_to_element(hoverele)
# action.perform()

#-------navbar elemnt---------

# mobilelink=driver.find_element(By.LINK_TEXT,"Mobiles")
# mobilelink.click()
# # checksamsung=driver.find_element(By.XPATH,'//li[@class="a-spacing-micro"]//span[1]//a[1]//div[1]/label[1]//i[1]')
# # checksamsung=driver.find_element(By.XPATH,'//*[@id="s-refinements"]/div[5]/ul/li[3]/span/a/div')
# checksamsung=driver.find_element(By.XPATH,'//*[@id="s-refinements"]/div[5]/ul/li[1]/span/a/span')
# checksamsung.click()
# selectmob=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[7]/div/div/div/div/div[1]/span/a').click()
# time.sleep(3)
# detail=driver.find_element(By.ID,'ap_container')

# # detail=driver.find_element(By.XPATH,'//span[@id="productTitle"]')
# # detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'centerCol')))
# print(detail)
# time.sleep(3)
# # detail.click()
# driver.quit()
# src=driver.page_source
# soup=BeautifulSoup(src,'lxml')
# print(soup.prettify())
# d=soup.find_all('span',class_='a-size-large product-title-word-break')
# print(d)

# for d in range(len(detail)):
#     print(d)
# sm=driver.find_element(By.CLASS_NAME,'a-link-normal s-no-outline')
# print(sm)
time.sleep(5)

# #-------select eleemnt---------
# searchdropdown=driver.find_element(By.ID,"searchDropdownBox")
# # searchdropdown.click()
# # book=driver.find_element(By.XPATH,"option[@value='search-alias=stripbooks]")
# book=driver.find_element(By.XPATH,"//option[@value='search-alias=stripbooks']")
# # action.click(searchdropdown)
# # action.click(book)
# select_book=Select(searchdropdown)
# select_book.select_by_value("search-alias=stripbooks")

# #-------open menu and close menu---------
# menu=driver.find_element(By.ID,"nav-hamburger-menu")
# menu.click()
# closemenu=driver.find_element(By.XPATH,"//div[@class='nav-sprite hmenu-close-icon']")
# closemenu.click()


# #----------hover on prime----------
# primeelement=driver.find_element(By.ID,"nav-link-amazonprime")
# action.move_to_element(primeelement)
# action.perform()




# #----------next picture---------
# for i in range(1,4):
#     np=driver.find_element(By.XPATH,"//div[@id='gw-desktop-herotator']//div[1]//div[1]//div//div[3]//a[1]")
#     np.click()
#     time.sleep(2)


# #--------back to homepage----------
# home=driver.find_element(By.ID,"nav-logo-sprites").click()
# time.sleep(5)

# #-------sign-in--------
# acc_list=driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']//span[1]")
# action.move_to_element(acc_list)
# sign_in=driver.find_element(By.XPATH,"//div[@id='nav-flyout-ya-signin']//a[1]")
# action.click(sign_in)
# action.perform()
# # creteac=driver.find_element(By.XPATH,"//div[@id='a-page']//div[1]//div[2]//div[1]//div[2]//div[1]//span[1]//span[1]")
# createac=driver.find_element(By.ID,'createAccountSubmit')
# createac.click()

# #filling form------
# name=driver.find_element(By.ID,'ap_customer_name')
# name.send_keys('abc')
# select_cc=driver.find_element(By.ID,'auth-country-picker')
# selectcc=Select(select_cc)
# selectcc.select_by_value('IN')
# mon=driver.find_element(By.ID,'ap_phone_number')
# mon.send_keys('9876543212')
# email=driver.find_element(By.ID,'ap_email')
# email.send_keys('nl.empiric@gmail.com')
# psw=driver.find_element(By.ID,'ap_password')
# psw.send_keys('1234567')
# submit=driver.find_element(By.ID,'auth-continue')
# submit.click()
# time.sleep(5)
# #back to homepage----------
# home=driver.find_element(By.CLASS_NAME,"a-link-nav-icon").click()
# time.sleep(5)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollBy(0,1500)", "")
time.sleep(5)



# driver.close()