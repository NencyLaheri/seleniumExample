from selenium import webdriver
import random
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
# from selenium.webdriver.chrome.options import ChromeOp
from selenium.webdriver.support.wait import WebDriverWait



ch_options = webdriver.ChromeOptions()
ch_options.add_argument("--disable-web-security")
# ch_options.add_argument("--window-size=800,600")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ch_options)
driver.maximize_window()
driver.get("https://www.linkedin.com/login")
# driver.implicitly_wait(5)
time.sleep(5)
# username = driver.find_element(By.XPATH,'//*[@id="username"]')
# username.send_keys("9099480276")

# pwd = driver.find_element(By.XPATH,'//*[@id="password"]')
# pwd.send_keys("urmi@0015") 

# submit = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
# submit.click()

# time.sleep(10)

# #search button
# search = driver.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input')
# time.sleep(2)
# search.send_keys('python')
# search.send_keys(Keys.ENTER)
# time.sleep(10)

# #people filter 
# people = driver.find_elements(By.XPATH,'//li[@class="search-reusables__primary-filter"]')
# for i in people:
#     print(i.text)
#     if i.text == "People":
#         print("----------------------",i.text)
#         time.sleep(3)
#         i.click()
#         time.sleep(3)
#         break

# profile_link_array=[]
# name_array=[]
# city_array=[]
# experience_array=[]
# company_name_array=[]

# # Current_company filter
# Current_company = driver.find_elements(By.XPATH,'//div[@class="search-reusables__filter-trigger-and-dropdown"]/span/button')
# time.sleep(2)
# for i in Current_company:
#     print(i.text)
#     if i.text == "Current company":
#         i.send_keys(Keys.ENTER)
#         search_company=driver.find_element(By.XPATH,'//div[@class="search-basic-typeahead search-vertical-typeahead"]/input[@placeholder="Add a company"]')
#         search_company.send_keys("empiric infotech")
#         search_company.click()
#         time.sleep(3)
#         type_name_enter=driver.find_element(By.XPATH,"//div[@class='basic-typeahead__triggered-content ']/div/div[1]/div/span/span").click()
#         time.sleep(3)
#         print("--------------------------",type_name_enter)
#         span_show_button= i.find_elements(By.XPATH,'//div[@class="reusable-search-filters-buttons display-flex justify-flex-end mt3 ph2"]/button/span')
#         for j in span_show_button:
#             print(j.text)
#             if j.text == "Show results":
#                 j.click()
#         time.sleep(2)
#         break
#     time.sleep(2)
# time.sleep(2)

# # location filter
# location = driver.find_elements(By.XPATH,'//div[@class="search-reusables__filter-trigger-and-dropdown"]/span/button')
# for j in location:
#     time.sleep(5)
#     if j.text == "Locations":
#         j.send_keys(Keys.ENTER)
#         box=(driver.find_element(By.XPATH,'//div[@class="search-basic-typeahead search-vertical-typeahead"]/input[@placeholder="Add a location"]'))
#         box.send_keys('Surat')
#         box.click()
#         time.sleep(1)
#         print("-----------------------------------")
#         #location dropdown.
#         location1= driver.find_elements(By.XPATH,'//div[@class="search-basic-typeahead search-vertical-typeahead"]//following-sibling::*')
#         for i in location1:
#             if i.text == "Surat, Gujarat, India":
#                 i.click()
#                 time.sleep(1)
#                 #drop down show_results button
#                 span = j.find_elements(By.XPATH,'//div[@class="reusable-search-filters-buttons display-flex justify-flex-end mt3 ph2"]/button/span')
#                 for k in span:
#                     if k.text == "Show results":
#                         k.click()
#                         time.sleep(1)
#                         break
#                     time.sleep(1)
#                 break  
#             time.sleep(1)   
#         break
#     time.sleep(1)

# #user profile_links
# profile =(driver.find_elements(By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link"]'))
# for i in profile:
#     profile_link_array.append(i.get_attribute("href"))
#     time.sleep(1)


# profile_link = len(driver.find_elements(By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link"]'))
# print("profile_link",profile_link)
# count = 0
# time.sleep(2)

# while (count < profile_link):
#     #click on profile link
#     profile = driver.find_elements(By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link"]')
#     profile[count].click() 
#     try:
#         #User name
#         user_name = driver.find_element(By.XPATH,'//div[@class="mt2 relative"]/div/div/h1')
#         name_array.append(user_name.text)
#         time.sleep(2)

#         #find city of user
#         city = driver.find_element(By.XPATH,'//span[@class="text-body-small inline t-black--light break-words"]')
#         city_array.append(city.text)
        
#         #find experience
#         experience = driver.find_element(By.XPATH,'//div[@id="experience"]//following-sibling::div/ul/li/div/div[2]/div[1]/div[1]/div/span/span[1]')
#         experience_array.append(experience.text)

#         #find comapany name
#         company = driver.find_element(By.XPATH,'//div[@id="experience"]//following-sibling::div/ul/li/div/div[2]/div[1]/div[1]/span[1]/span[1]') 
#         company_name_array.append(company.text)
#         time.sleep(1)
#         count +=1
#         time.sleep(1)
#         driver.back()
#     except :
#         print("+++++++++++++++++++++")
#         dialog = driver.find_element(By.XPATH,"//div[@class='artdeco-modal artdeco-modal--layer-default ']")
#         time.sleep(2)
#         button = driver.find_element(By.XPATH,'//button[@class="fr artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]/span').click()
#         # time.sleep(2)
#         count +=1


# # print("++++++++++++++++++++++++++++",name_array)
# # print("++++++++++++++++++++++++++++",city_array)
# # print("++++++++++++++++++++++++++++",profile_link_array)
# # print("++++++++++++++++++++++++",experience_array)
# # print("+++++++++++++++++++++++++++++",company_name_array)

# #create csv and store data in csv 
# file = open('linkedin.csv', 'w', newline='')
# with file: 
#     writer = csv.writer(file,delimiter='\t')
#     writer.writerow(['Name' ,'City' ,'profile link','experience','company']) 
#     for i in zip(name_array,city_array,profile_link_array,experience_array,company_name_array):
#         writer.writerow(i)
# time.sleep(2)  

# home = driver.find_element(By.XPATH,'//div[@class="global-nav__content"]/nav/ul/li[1]/a/span')
# home.click()
# time.sleep(2)

# #find body tag
# body=driver.find_element(By.TAG_NAME,"body")
# for i in range(0,1):
#     body.send_keys(Keys.END)
#     print("====================")
#     time.sleep(5)
# # scroll=0  
# # height=driver.execute_script("return document.body.scrollHeight") 
# # finalScroll=(height * 4) 

# # print("height",height)
# # while True:
# #     driver.execute_script(f"window.scrollTo({scroll},{finalScroll})")
# #     scroll += height
# #     time.sleep(1)
# #     if scroll == finalScroll:
# #         break
# # abc= input()
# time.sleep(2)

# like_button = driver.find_elements(By.XPATH,'//div[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[1]/button[1]')
# comment_button = driver.find_elements(By.XPATH,'//div[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[2]/span/div/button[1]')
# print("***********************",len(comment_button))
# print("------------------",len(like_button))
# time.sleep(5)

# for j in comment_button:
#     comment= [True,False]
#     comment_choice=random.choice(comment)
#     print("++++++++++++++++++++++++++++++++")
#     driver.execute_script("arguments[0].click();", j)
#     print("comment_box")
#     time.sleep(1)
    
# comment_box = driver.find_elements(By.XPATH,'//div[@class="comments-comment-box__form-container flex-grow-1"]/form/div/div/div[1]/div/div[2]/div/div/div[1]/p')

# for i,k in zip(like_button,comment_box):
#         like= [True,False]
#         comment= [True,False]
#         comment_choice=random.choice(comment)
#         like_choice=random.choice(like)
#         print("like_choice",like_choice)
#         print("comments_choice",comment_choice)
#         if like_choice == True:
#             print("=================================",i.get_attribute("aria-pressed"))
#             if i.get_attribute("aria-pressed") == "false":
#                 time.sleep(5)
#                 print("*******************",i)
#                 driver.execute_script("(arguments[0]).click();", i)
#                 # abc= input() 
#                 time.sleep(5)
#         if comment_choice == True:
#             time.sleep(5)
#             print("---------------------------------",k)
#             k.send_keys("great")
#             post_button = driver.find_element(By.XPATH,'//button[@class="comments-comment-box__submit-button mt3 artdeco-button artdeco-button--1 artdeco-button--primary ember-view"]')
#             print("====================post_button",post_button)
#             time.sleep(3)
#             driver.execute_script("(arguments[0]).click();", post_button)
#             time.sleep(5)
# abc= input()                       
       