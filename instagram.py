# # # # import time
# # # # import requests
# # # # from selenium import webdriver
# # # # from selenium.webdriver.chrome.service import Service as ChromeService
# # # # from selenium.webdriver.chrome.service import Service
# # # # from webdriver_manager.chrome import ChromeDriverManager
# # # # from selenium.webdriver.common.keys import Keys
# # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # from selenium.webdriver.common.by import By
# # # # from selenium.webdriver.support import expected_conditions as EC
# # # # from selenium.webdriver.common.action_chains import ActionChains
# # # # from bs4 import BeautifulSoup



# # # # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# # # # driver.get("https://www.instagram.com/login/")
# # # # # abc=input()
# # # # time.sleep(5)
# # # # username= driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[1]/div/label/input')
# # # # username.send_keys("patelurmila15898@gmail.com")
# # # # password = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[2]/div/label/input')
# # # # password.send_keys("meurmi@1998")
# # # # login_btn = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[3]')
# # # # login_btn.click()
# # # # time.sleep(25)
# # # # # not_now_btn = driver.find_element(By.XPATH,'//div[@class="bdao358l om3e55n1 g4tp4svg"]/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
# # # # # not_now_btn.click()
# # # # search = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
# # # # search.send_keys('virat kohli')
# # # # driver.maximize_window()
# # # # time.sleep(3)
# # # # search_list = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/a')
# # # # search_list.click()
# # # # time.sleep(5)
# # # # # abc= input()
# # # # # post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article[1]/div/div/div[1]/div/a')
# # # # # time.sleep(2)
# # # # # for i in post:
# # # # #     print(i.get_attribute("href"))
# # # # # # post_hef = post.get_attribute("href")
# # # # # print(post)
# # # # # print(post_hef)


# # # # # post=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="_aagu"]')))
# # # # post=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="_aabd _aa8k _aanf"]/a')))
# # # # print(post)
# # # # action=ActionChains(driver)
# # # # action.move_to_element(post).perform()
# # # # time.sleep(2)
# # # # print(post.get_attribute('href'))
# # # # time.sleep(10)


# # # # r = requests.get("https://www.instagram.com/virat.kohli/")
# # # # soup = BeautifulSoup(r.text, 'lxml')
# # # # # print(soup.prettify())
# # # # # print(r.content)
# # # # print(soup.find_all('a'))

# # # # abc=input()




# # # #-------------------------------------------

# # # import time
# # # import requests
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service as ChromeService
# # # from selenium.webdriver.chrome.service import Service
# # # from webdriver_manager.chrome import ChromeDriverManager
# # # from selenium.webdriver.common.keys import Keys
# # # from selenium.webdriver.common.by import By

# # # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# # # driver.get("https://www.instagram.com/login/")
# # # # abc=input()
# # # time.sleep(5)
# # # username= driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[1]/div/label/input')
# # # username.send_keys("patelurmila15898@gmail.com")
# # # password = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[2]/div/label/input')
# # # password.send_keys("meurmi@1998")
# # # login_btn = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[3]')
# # # login_btn.click()
# # # time.sleep(25)
# # # # not_now_btn = driver.find_element(By.XPATH,'//div[@class="bdao358l om3e55n1 g4tp4svg"]/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
# # # # not_now_btn.click()
# # # search = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
# # # search.send_keys('virat kohli')
# # # driver.maximize_window()
# # # time.sleep(3)
# # # search_list = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/a')
# # # search_list.click()
# # # time.sleep(5)
# # # # abc= input()
# # # body=driver.find_element(By.TAG_NAME,"body")
# # # for i in range(0,5):
# # #     body.send_keys(Keys.END)
# # #     print("====================")
# # #     time.sleep(5)

# # # post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article[1]/div/div/div/div/a')
# # # time.sleep(2)
# # # c=0
# # # for i in post:
# # #     print(c)
# # #     c+=1
# # #     print(i.get_attribute("href"))
# # # # post_hef = post.get_attribute("href")
# # # # print(post)
# # # # print(post_hef)
# # # abc=input()


# # #-------------------------
# # import time
# # import requests
# # import csv
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.action_chains import ActionChains



# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# # driver.get("https://www.instagram.com/login/")
# # # abc=input()
# # time.sleep(5)
# # # *********username textbox ******************
# # username= driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[1]/div/label/input')
# # username.send_keys("patelurmila15898@gmail.com")
# # # *********************psssword textbox******************
# # password = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[2]/div/label/input')
# # password.send_keys("meurmi@1998")
# # # ***************login button***************
# # login_btn = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[3]')
# # login_btn.click()
# # time.sleep(25)
# # # not_now_btn = driver.find_element(By.XPATH,'//div[@class="bdao358l om3e55n1 g4tp4svg"]/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
# # # not_now_btn.click()
# # # *********************search button **********************

# # search = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
# # search.send_keys('virat kohli')
# # driver.maximize_window()
# # time.sleep(3)
# # # *****************search list ******************
# # search_list = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/a')
# # search_list.click()
# # # time.sleep(5)
# # # abc= input()

# # time.sleep(10)
# # # ****************scrolled down page****************
# # # body=driver.find_element(By.TAG_NAME,"body")
# # # for i in range(0,5):
# # #     body.send_keys(Keys.END)
# # #     print("====================",i)
# # #     time.sleep(5)
# # # ************click on post and find likes ******************
# # # c=0
# # # post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article[1]/div/div/div/div/a')
# # # print(len(post))
# # # time.sleep(20)
# # # for i in post:
# # #     print(c)
# # #     c+=1
# # #     print(i.get_attribute("href"))
# # #     i.click()
# # #     time.sleep(3)
# # #     likes = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a/div/span')
# # #     print("=============",likes.text,"-------------------")
# # #     driver.back()
# # #     time.sleep(3)
# # # time.sleep(10)
# # # ******************mouse hover post and find likes **************************
# # # c=0
# # # action=ActionChains(driver)
# # # post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a')
# # # for i in post:
# # #     time.sleep(5)
# # #     print(c)
# # #     c+=1
# # #     print(i.get_attribute("href"))
# # #     i.send_keys(Keys.ARROW_UP)
# # #     # action.move_to_element(i).perform()
# # #     time.sleep(10)
# # #     # focus = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a/div[@class="_ac2d"]/ul/li/div/span')))
# # #     focus=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0_3X"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[3]/ul/li[1]/div/span')))
# # #     print(focus)
# # #     time.sleep(3)
# # # # abc= input()
# # #     print("++++++++++++++++++++",focus.text,"++++++++++++")
# # #     time.sleep(3)

# # # abc= input()
# # #--------------------------------------------------------------
# # post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a')
# # action=ActionChains(driver)
# # print(len(post))
# # i=0
# # while i < len(post):
# #     post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a')
# #     p=post[i]
# #     # p.send_keys(Keys.ARROW_UP)
# #     action.move_to_element(p).perform()
# #     time.sleep(2)
# #     focus=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0_3X"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[3]/ul/li[1]/div/span')))
# #     print(focus)
# #     time.sleep(3)
# #     i+=1



# # #--------------------------------------------------------------
# # # file = open('instagram.csv', 'w', newline='')
# # # with file: 
# # #     writer = csv.writer(file,delimiter='\n')
# # #     writer.writerow(['Posts']) 
# # #     # for i in posts:
# # #     writer.writerow(posts)
# # # time.sleep(2)  


# # abc=input()




# #-------------metaaaa----------------
# import time
# import requests
# import csv
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.instagram.com/login/")
# # abc=input()
# time.sleep(5)
# # *********username textbox ******************
# username= driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[1]/div/label/input')
# username.send_keys("shahurmila.shah")

# # *********************psssword textbox******************
# password = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[2]/div/label/input')
# password.send_keys("meurmi@1998")

# # abc= input()
# # ***************login button***************
# login_btn = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[3]')
# login_btn.click()
# time.sleep(25)

# # *********************search button **********************
# search = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
# search.send_keys('virat.kohli')
# driver.maximize_window()
# time.sleep(3)

# # *****************search list ******************
# search_list = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/a')
# search_list.click()
# # time.sleep(5)
# # abc= input()
# time.sleep(20)

# # ****************scrolled down page****************
# # body=driver.find_element(By.TAG_NAME,"body")
# # for i in range(0,2):
# #     body.send_keys(Keys.END)
# #     print("====================",i)
# #     time.sleep(5)
# # ************click on post and find likes ******************
# c=0
# post1 = []
# posts = []
# likes = []
# comments = [] 
# post = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article[1]/div/div/div/div/a')
# print((post))
# post_link = post.get_attribute("href")
# print(post.get_attribute("href"))
# posts.append(post_link)
# time.sleep(3)
# post.click()
# time.sleep(3)
# like = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a/div/span')
# likes_count = like.text
# likes.append(likes_count)
# print("=============",like.text,"-------------------")
# time.sleep(10)
# # abc=input()
# div= driver.find_element(By.XPATH,'//article[@class="_aatb _aate _aatg _aati"]/div/div[2]/div/div/div[2]/div[1]')
# print("----------div------",div)
# time.sleep(10)
# scroll = 0
# while scroll < 5: # scroll 5 times
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', div)
#     print("------------------------")
#     time.sleep(2)
#     scroll += 1

# time.sleep(10)
# comment = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/ul/div/li/div/div/div[2]/h3/div/span/a')
# # print("=============",likes.text,"-------------------")
# for i in comment:
#     cmt_links = i.get_attribute("href")
#     comments.append(cmt_links)
#     print(cmt_links)


# post1.append(posts)
# post1.append(likes)
# post1.append(comments)

# print("-------------------------------post1",post1)
#     # print(i.text)
# # time.sleep(20)
# # for i in post:
# #     print(c)
# #     c+=1
# #     print(i.get_attribute("href"))
# #     i.click()
# #     time.sleep(3)
# #     likes = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a/div/span')
# #     print("=============",likes.text,"-------------------")
# #     comments = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/ul/div/li/div/div/div[2]/h3/div/span/a')
# #     for i in comments:
# #         print(i.get_attribute("href"))
# #         print(i.text)
# #     driver.back()
# #     time.sleep(3)
# # time.sleep(10)
# # ******************mouse hover on post and find likes **************************
# c=0
# liked = []
# comments = []
# # driver.execute_script("window.scrollBy(0,1000000)")
# time.sleep(20)
# # post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a')
# # print(len(post))
# # for i in post:
# #     time.sleep(3)
# #     print(c)
# #     c+=1
# #     print(i.get_attribute("href"))
# #     i.send_keys(Keys.ARROW_UP)
# #     time.sleep(3)
# #     focus = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a/div[@class="_ac2d"]/ul/li/div/span')
# #     time.sleep(3)
# #     commnt = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a/div[@class="_ac2d"]/ul/li[2]/div/span')
# #     time.sleep(3)
# #     cd = commnt.text
# #     ab = focus.text
# #     time.sleep(5)
# #     # liked.append(ab)
# #     # comments.append(cd)
# #     print("++++++++++++++++++++",ab,"++++++++++++")
# #     print("------------------",cd,"-----------")
# #     time.sleep(3)
    
# print(liked)
# print(comments)
# # abc= input()
# file = open('insta.csv', 'w', newline='')
# with file: 
#     writer = csv.writer(file,delimiter='\n')
#     writer.writerow(['Posts','likes','comment']) 
#     # for i in posts:
#     writer.writerow(post1)
# time.sleep(2)  




#---------------------------------------------------------------------------------------------------------------------------------------------
import time
import requests
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/login/")
# abc=input()
time.sleep(20)
# *********username textbox ******************
username= driver.find_element(By.XPATH,'//form[@class="_ab3b"]//div/div/div/label/input')
username.send_keys("patelurmila15898@gmail.com")

# *********************psssword textbox******************
password = driver.find_element(By.XPATH,'//form[@class="_ab3b"]/div/div[2]/div/label/input')
password.send_keys("meurmi@1998")

# abc= input()
# ***************login button***************
login_btn = driver.find_element(By.XPATH,'//form[@class="HmktE"]/div/div[3]')
login_btn.click()

driver.maximize_window()
time.sleep(35)
# *********************search button **********************
search = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('virat.kohli')

time.sleep(3)

# *****************search list ******************
search_list = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/a')
search_list.click()
# time.sleep(5)
# abc= input()
time.sleep(20)

# ****************scrolled down page****************
# body=driver.find_element(By.TAG_NAME,"body")
# for i in range(0,2):
#     body.send_keys(Keys.END)
#     print("====================",i)
#     time.sleep(5)
# ************click on post and find likes ******************
c=0
a=0
posts = []
likes = []
comments = [] 
post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article[1]/div/div/div/div/a')
print(len(post))
# time.sleep(20)
obj = {}
for i in post:
    print(c)
    c+=1
    post_link = i.get_attribute("href")
    # print(i.get_attribute("href"))
    posts.append(post_link)
    i.click()
    time.sleep(5)
    like = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a/div/span')
    like_count = like.text
    likes.append(like_count)
    print("=============",like.text,"-------------------")
    comment = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/ul/div/li/div/div/div[2]/h3/div/span/a')
    for i in comment:
        # print(len(comment))
        # a+=1
        cmt_user = i.get_attribute("href")
        print(cmt_user)
        comments.append(cmt_user)
        obj[str(a)] = []
    obj[str(a)]+=comments
    a+=1
            # print(i.text)
    # print("******************************comments",comments)         
    # print("*********************-----------------***************obj",obj)
    time.sleep(3)
    driver.back()
    comments.clear()
    time.sleep(3)
print("******************************obj") 
print(obj)
print("----------------------------posts")
print(posts)
# time.sleep(10)
# ******************mouse hover on post and find likes **************************
# c=0
# liked = []
# comments = []
# driver.execute_script("window.scrollBy(0,1000000)")
time.sleep(20)
# post = driver.find_elements(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a')
# print(len(post))
# for i in post:
#     time.sleep(3)
#     print(c)
#     c+=1
#     print(i.get_attribute("href"))
#     i.send_keys(Keys.ARROW_UP)
#     time.sleep(3)
#     focus = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a/div[@class="_ac2d"]/ul/li/div/span')
#     time.sleep(3)
#     commnt = driver.find_element(By.XPATH,'//div[@class="x9f619 x1n2onr6 x1ja2u2z"]/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div/div/a/div[@class="_ac2d"]/ul/li[2]/div/span')
#     time.sleep(3)
#     cd = commnt.text
#     ab = focus.text
#     time.sleep(5)
#     # liked.append(ab)
#     # comments.append(cd)
#     print("++++++++++++++++++++",ab,"++++++++++++")
#     print("------------------",cd,"-----------")
#     time.sleep(3)
print("******************************likes")   
print(likes)
print("******************************obj") 
print(obj)
print("----------------------------posts")
print(posts)

abc= input()
file = open('post1.csv', 'w', newline='')
with file: 
    writer = csv.writer(file,delimiter='\t')
    writer.writerow(['Posts','likes','comments']) 
    # for i in posts:
    for j,k in obj.items():
        writer.writerow([posts,likes,k])
    # writer.writerow(posts)

time.sleep(2)  
