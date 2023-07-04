from argparse import Action
from audioop import add
from cgitb import text
from time import sleep, time
from xml.dom.minidom import Document
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import csv 
import xlsxwriter     




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
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# driver=webdriver.Chrome(service=path)
driver.get('https://www.linkedin.com/login')
# driver.get('https://www.linkedin.com/feed/')
# driver.maximize_window()
action=ActionChains(driver)
#------print title----------
print(driver.title)

#---------login----------
email=driver.find_element(By.ID,'username')
password=driver.find_element(By.ID,'password')
email.send_keys("sd.empiric@gmail.com")
password.send_keys('SD090721@Empiric')
signin=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
signin.click()
time.sleep(15)
# home_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//header[@id="global-nav"]/div/a/div/div/li-icon')))
# # home_page=driver.find_element(By.XPATH,'//header[@id="global-nav"]/div/a/div/div/li-icon')
# action.move_to_element(home_page).perform()
# action.click(home_page).perform()
# time.sleep(10)
# driver.refresh()


# #-----scroll------
# for u in range(1):
#     driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)
#     time.sleep(5)


# #--------viewprofile------
# # profilebtn=driver.find_element(By.XPATH,'//header[@id="global-nav"]/div/nav/ul/li[6]')
# profilebtn=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//header[@id="global-nav"]/div/nav/ul/li[6]')))
# print(profilebtn)
# driver.execute_script("arguments[0].click();",profilebtn)
# # profilebtn.click()
# time.sleep(2)
# viewprofile=driver.find_element(By.XPATH,'//*["ember19"]/div[1]/header').click()


# # -------like all post--------
# likebtn=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[1]/button[1]')))
# for i in range(0,len(likebtn)):
#     try:
#         time.sleep(3)
#         action.move_to_element(likebtn.__getitem__(i)).perform()
#         time.sleep(1)
#         # print(likebtn.__getitem__(i))
#         # likebtn.__getitem__(i).click()
#         if likebtn.__getitem__(i).get_attribute("aria-pressed")=="false":
#             likebtn.__getitem__(i).click()
#             time.sleep(2)
#     except:
#         pass
#     time.sleep(2)

# # #---------------------------
# # like_buttons = driver.find_elements(By.XPATH, "//div[@class='social-details-social-activity update-v2-social-activity']/div[2]/span/button[1]")
# # print(len(like_buttons))
# # for l_button in like_buttons: 
# #     driver.execute_script("arguments[0].scrollIntoView();", l_button)
# #     action.move_to_element(l_button).perform()
# #     action.click(l_button).click()
# #     time.sleep(2)
# # 


# #---------like random post--------
# likebtn=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[1]/button[1]')))
# r=['True','False']
# for i in range(0,len(likebtn)):
#     rd=random.choice(r)
#     # print(rd)
    
#     try:
#         time.sleep(3)
#         action.move_to_element(likebtn.__getitem__(i)).perform()
#         time.sleep(1)
#         if rd=='True':
#             if likebtn.__getitem__(i).get_attribute("aria-pressed")=="false":
#                 likebtn.__getitem__(i).click()
#                 print('--clicked--')
#                 time.sleep(2)
#     except:
#         pass
#     time.sleep(2)



# #----------comment on single post----------
# time.sleep(2)
# comment=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[2]/span[1]/div[1]/button[1]')))
# # comment=driver.find_element(By.XPATH,'//div[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[2]/span[1]/div[1]/button[1]')
# print(comment)
# action.move_to_element(comment).perform()
# action.click(comment).perform()
# time.sleep(2)
# cmt=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//form[@class="comments-comment-box__form"]/div/div/div[1]/div/div[2]/div/div/div[1]')))
# cmt.send_keys('.')
# time.sleep(2)
# postcmt=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//form[@class="comments-comment-box__form"]/div[2]/button')))
# action.move_to_element(postcmt).perform()
# action.click(postcmt).perform()


# # --------comment on all post-----
# rcmt=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[2]/span[1]/div[1]/button[1]')))
# for i in range(0,len(rcmt)):
#     action.move_to_element(rcmt.__getitem__(i)).perform()
#     action.click(rcmt.__getitem__(i)).perform()
#     time.sleep(2)
#     cmt = driver.find_elements(By.XPATH,'//div[@class="comments-comment-box__form-container flex-grow-1"]/form/div/div/div/div/div[2]/div/div/div/p')
#     v=cmt.__getitem__(i)
#     print(v)
#     v.send_keys('great')
#     time.sleep(2)
#     postcmt=driver.find_element(By.XPATH,'//form[@class="comments-comment-box__form"]/div[2]/button')
#     action.move_to_element(postcmt).perform()
#     action.click(postcmt).perform()
#     time.sleep(2)


# #---------comment random post--------
# rcmt=driver.find_elements(By.XPATH,'//div[@class="social-details-social-activity update-v2-social-activity"]/div[2]/span[2]/span[1]/div[1]/button[1]')
# print('--comment--',len(rcmt))
# r=['True','False']
# for i in range(0,len(rcmt)):
#     action.click(rcmt.__getitem__(i)).perform()
#     time.sleep(2)
#     rd=random.choice(r)
#     print(rd)
#     if rd=='True':
#         cmt = driver.find_elements(By.XPATH,'//div[@class="comments-comment-box__form-container flex-grow-1"]/form/div/div/div/div/div[2]/div/div/div/p')
#         v=cmt.__getitem__(i)
#         # print(v)
#         v.send_keys('great')
#         time.sleep(2)
#         postcmt=driver.find_element(By.XPATH,'//form[@class="comments-comment-box__form"]/div[2]/button')
#         action.move_to_element(postcmt).perform()
#         action.click(postcmt).perform()
#         time.sleep(2)



# #---------search-------
# print(search)
# search.send_keys('surat')
name=[]
country=[]
company=[]
with open('userdetails.csv','r') as c:
    cr=csv.reader(c)
    next(cr)
    for cdata in cr:
        i=cdata
        # print(len(i[0]))
        # print(i[0])
        name.append(i[0])
        country.append(i[2]) 
        company.append(i[3])


# for i in name:
#     search=driver.find_element(By.XPATH,'//div[@id="global-nav-typeahead"]/input[1]')

#     search.send_keys(i)
#     search.send_keys(Keys.ENTER)
#     time.sleep(1)
#     continue

# i=0
# while i < len(name):
#     search=driver.find_element(By.XPATH,'//div[@id="global-nav-typeahead"]/input[1]')
#     search.send_keys(name[i])
#     search.send_keys(Keys.ENTER)
#     time.sleep(1)
#     i+=1

dname=[]
ddetail=[]
companyname=[]
exp=[]

def search(keyword):
    search=driver.find_element(By.XPATH,'//div[@id="global-nav-typeahead"]/input[1]')
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)
    time.sleep(5)
    people=driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul[1]/li[1]/button')
    # print('people:---------',people)
    action.move_to_element(people).perform()
    action.click(people).perform()
    time.sleep(2)

    #----------location-----------
    # location=driver.find_element(By.XPATH,'//*[@id="ember730"]/button')
    # location=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@id="search-reusables__filters-bar"]/ul/li[4]/div/span/button')))
    # # print('location----------',location)
    # action.move_to_element(location).perform()
    # time.sleep(2)
    # action.click(location).perform()

    # time.sleep(2)
    # # addloc=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//div[@id="artdeco-hoverable-artdeco-gen-82"]')))
    # addloc=driver.find_element(By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form/fieldset/div/div/div/input')
    # # print(addloc)
    # addloc.send_keys('surat')
    # time.sleep(3)
    # addloc.send_keys(Keys.ENTER)
    # addloc.click()
    # # selectloc=driver.find_elements(By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form//div/div/div/div[2]/div/div')
    # # selectloc=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form//div/div/div/div[2]/div/div/div/span/span')))
    # # time.sleep(2)
    # selectloc=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form//div/div/div/div[2]/div/div[1]/div/span/span'))).click()
    # # print(selectloc)
    # showresult=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form//div[2]/button[2]')))
    # action.move_to_element(showresult).perform()


    #---company name-----
    current_company=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@id="search-reusables__filters-bar"]/ul/li[5]/div/span/button')))
    # print('current company:----------',current_company)
    action.click(current_company).perform()
    add_company=driver.find_element(By.XPATH,'//div[@id="hoverable-outlet-current-company-filter-value"]/div/div/div/form/fieldset/div/div/div/input')
    # print('add comapany:-----------',add_company)
    add_company.send_keys('empiric infotech')
    time.sleep(2)
    select_company=driver.find_element(By.XPATH,'//div[@id="hoverable-outlet-current-company-filter-value"]/div/div/div/form/fieldset/div/div/div/div[2]/div/div/div/span/span').click()
    # print('select company:----',select_company)
    time.sleep(2)
    cshowresult=driver.find_element(By.XPATH,'//div[@id="hoverable-outlet-current-company-filter-value"]/div/div/div/form/fieldset/div[2]/button[2]')
    # print('cshowresult:-------',cshowresult)
    action.click(cshowresult).perform()
    time.sleep(2)


for i in name:
    search(i)
    profilelink=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link "]')))
    # print('profile link---------',profilelink)
    
    # profilelink.click()
    # # time.sleep(10)
    # # profilelink=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link "]')))
    # print('profiles:--------',profilelink)
    c=0
    while c < len(profilelink):
        
        profilelink=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link "]')))
        p=profilelink
        p[c].click()

        try:
            #-----get user-----
            print('----------------------')
            time.sleep(5)
            user=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//section[@class="artdeco-card ember-view pv-top-card"]/div[2]/div[2]/div[1]/div[1]/h1')))
            print('Name: ',user.text)
            n=user.text
            dname.append(n)

            #-----detail-----
            detail=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//section[@class="artdeco-card ember-view pv-top-card"]/div[2]/div[2]/div[1]/div[2]')))
            print('detail: ',detail.text)
            d=detail.text
            ddetail.append(d)


            #-----company name------
            company_name=driver.find_element(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li[1]/div/div[2]/div[1]//div[@class="display-flex align-items-center"]/span[1]/span[1]')
            # print('company name:-------',company_name)
            print('company name:  ',company_name.text)
            cm=company_name.text
            companyname.append(cm)

            #------experience------
            time.sleep(3)
            experience=driver.find_elements(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li/div/div[2]/div//div[@class="display-flex align-items-center"]/span/span[1]')
            exp_detail=driver.find_elements(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li/div/div[2]/div//div[@class="display-flex align-items-center"]/following-sibling::span[1]/span[@aria-hidden="true"]')
            
            lzip1=[]
            print('experience: ')
            for (e,d) in zip(experience,exp_detail):
                lzip=[]
                print('\t',e.text)
                print('\t',d.text,'\n')
                lzip .append(e.text)
                lzip.append(d.text)
                lzip1.append(lzip)
            exp.append(lzip1)

            driver.back()
            time.sleep(2)
            c+=1

        except:
            time.sleep(2)
            driver.back()
            c+=1


    time.sleep(3)
    home=driver.find_element(By.XPATH,'//header[@id="global-nav"]/div/a/div/div/li-icon')
    # print('home:----',home)
    home.click()
    time.sleep(5)
    

print('\nname:-----------',dname)
print('\ndetail:---------',ddetail)
print('\ncompany name:--------',companyname)
print('\nexperience:----------',exp)
print('\nlength of exp:',len(exp))

# -----------store data in csv file-------------
# with open('linkedin1.csv','w') as f:
#     writer=csv.writer(f)
#     writer.writerow(['name','detail','company name','experience'])
#     for i in range(0,len(dname)):
#         for j in range(0,len(exp[i])):
#             writer.writerow([dname[i],ddetail[i],companyname[i],exp[i][j]])


# # -----------store data in excel file-------------      
book = xlsxwriter.Workbook('Example2.xlsx')     
sheet = book.add_worksheet()     

# for i in range(0,len(exp)):
#     for j in range(0,len(exp[i])):
#         for row,row_data in enumerate(zip(dname,ddetail,companyname,exp[i][j])):
#             print('exp----',exp[i][j])
#             for col,col_data in enumerate(row_data):      
#                 sheet.write(row,col,col_data)

# for i in range(0,len(exp)):
#     for j in range(0,len(exp[i])):
#         print('all data-----',dname,ddetail,companyname,exp[i][j])
#         v=[dname,ddetail,companyname,exp[i][j]]
#         for row,row_data in enumerate(v):
#             print('row data---------',row_data)
#             for col,csol_data in enumerate(row_data):
#                 print('col data--------',col_data)
#                 sheet.write(row,col,col_data)


for row,row_data in enumerate(zip(dname,ddetail,companyname,str(exp))):
    for col,col_data in enumerate(row_data):
        sheet.write(row,col,col_data)

book.close()  

# row=0                                                                                             
# column=0
# for i,j,k in zip(dname,ddetail,companyname):
#     sheet.write(row, column , i)
#     sheet.write(row, column + 1, j)
#     sheet.write(row, column + 2, k)
#     for i, l in enumerate(exp):
#         for j, col in enumerate(l):
#             sheet.write(row, column + 3, str(col))
#     row += 1
# book.close() 

# #--------------
# search=driver.find_element(By.XPATH,'//div[@id="global-nav-typeahead"]/input[1]')
# search.send_keys("rahul dabhi")
# time.sleep(1)
# search.send_keys(Keys.ENTER)
# time.sleep(2)
# people=driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul[1]/li[1]/button')
# # print(people)
# action.move_to_element(people).perform()
# action.click(people).perform()
# time.sleep(5)
# # location=driver.find_element(By.XPATH,'//*[@id="ember730"]/button')
# location=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@id="search-reusables__filters-bar"]/ul/li[4]/div/span/button')))
# # print(location)
# action.move_to_element(location).perform()
# time.sleep(2)
# action.click(location).perform()

# time.sleep(2)
# # addloc=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//div[@id="artdeco-hoverable-artdeco-gen-82"]')))
# addloc=driver.find_element(By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form/fieldset/div/div/div/input')
# # print(addloc)
# addloc.send_keys('surat')
# time.sleep(3)
# # addloc.send_keys(Keys.ENTER)
# # addloc.click()
# # selectloc=driver.find_elements(By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form//div/div/div/div[2]/div/div')
# # selectloc=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form//div/div/div/div[2]/div/div/div/span/span')))
# # time.sleep(2)
# selectloc=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form//div/div/div/div[2]/div/div[1]/div/span/span'))).click()
# # print(selectloc)
# showresult=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form//div[2]/button[2]')))
# action.move_to_element(showresult).perform()
# time.sleep(2)
# action.click(showresult).perform()


##------select companu--------
#current_company=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@id="search-reusables__filters-bar"]/ul/li[5]/div/span/button'))).click()
# add_company=driver.find_element(By.XPATH,'//div[@id="hoverable-outlet-current-company-filter-value"]/div/div/div/form/fieldset/div/div/div/input')
# add_company.send_keys('empiric infotech')
# time.sleep(2)
# select_company=driver.find_element(By.XPATH,'//div[@id="hoverable-outlet-current-company-filter-value"]/div/div/div/form/fieldset/div/div/div/div[2]/div/div/div/span/span').click()
# time.sleep(2)
# cshowresult=driver.find_element(By.XPATH,'//div[@id="hoverable-outlet-current-company-filter-value"]/div/div/div/form/fieldset/div[2]/button[2]').click()


# # ##-------profle link----------
# # name=[]
# # companyname=[]
# # lexperience=[]
# # ldexperience=[]

# time.sleep(10)
# profilelink=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link "]')))
# print('profiles:--------',profilelink)
# c=0
# while c<len(profilelink):
    
#     profilelink=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link "]')))
#     p=profilelink
#     p[c].click()

#     try:
#         #-----get user-----
#         print('----------------------')
#         time.sleep(5)
#         user=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//section[@class="artdeco-card ember-view pv-top-card"]/div[2]/div[2]/div[1]/div[1]/h1')))
#         print('Name: ',user.text)
#         # name.append(user.text)

#         #-----company name----
#         company_name=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//section[@class="artdeco-card ember-view pv-top-card"]/div[2]/div[2]/div[1]/div[2]')))
#         print('company Name: ',company_name.text)
#         # companyname.append(company_name.text)


#         #------experience------
#         time.sleep(3)
#         experience=driver.find_elements(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li/div/div[2]/div//div[@class="display-flex align-items-center"]/span/span[1]')
#         exp_detail=driver.find_elements(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li/div/div[2]/div//div[@class="display-flex align-items-center"]/following-sibling::span[1]/span[@aria-hidden="true"]')
        
#         # lzip1=[]
#         print('experience:')
#         for (e,d) in zip(experience,exp_detail):
#             # lzip=[]
#             print('\t',e.text)
#             print('\t',d.text,'\n')
#         #     lzip.append(e.text)
#         #     lzip.append(d.text)
#         #     lzip1.append(lzip)
#         # lexperience.append(lzip1)

#         driver.back()
#         time.sleep(2)
#         c+=1

#     except:
#         time.sleep(2)
#         driver.back()
#         c+=1


# # print('name:',name)
# # print('company name:',companyname)
# # print('experience:',lexperience)
# # print('experience detail:',ldexperience)


# # workbook = xlwt.Workbook() 
# # sheet = workbook.add_sheet("Sheet1")
# # # sheet.write(0,0,'Name')
# # # sheet.write(0,1,'Company Name')
# # # sheet.write(0,2,'experience')


# # for i in range(0,len(name)):
# #     sheet.write(1,0,name[i])

# # workbook.save('xlwt example.xls')



# #----------
# profilelink=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link"]')))
# # print(profilelink)
# time.sleep(2)
# profilelink.click()
# time.sleep(3)
# experience=driver.find_elements(By.XPATH,'//div[@id="experience"]/following-sibling::div[2]/ul/li/div/div[2]/div//div[@class="display-flex align-items-center"]/span/span[1]')
# for e in experience:
#     print(e)


#-----------

# profile_link=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link"]')))

# # profile_link = len(driver.find_elements(By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link"]'))
# print("profile_link",len(profile_link))
# count = 0
# time.sleep(2)

# while (count < len(profile_link)):
#     #click on profile link
#     profile = driver.find_elements(By.XPATH,'//div[@class="t-roman t-sans"]//a[@class="app-aware-link"]')
#     profile[count].click() 
#     print('in loop-------------------')
#     try:
#         #User name
#         user_name = driver.find_element(By.XPATH,'//div[@class="mt2 relative"]/div/div/h1')
#         print(user_name.text)
#         time.sleep(2)

        # #find city of user
        # city = driver.find_element(By.XPATH,'//span[@class="text-body-small inline t-black--light break-words"]')
        # (city.text)
        
        # #find experience
        # experience = driver.find_element(By.XPATH,'//div[@id="experience"]//following-sibling::div/ul/li/div/div[2]/div[1]/div[1]/div/span/span[1]')
        # print(experience.text)

        # #find comapany name
        # company = driver.find_element(By.XPATH,'//div[@id="experience"]//following-sibling::div/ul/li/div/div[2]/div[1]/div[1]/span[1]/span[1]') 
        # print(company.text)
        # time.sleep(1)
        # count +=1
        # time.sleep(1)
        # driver.back()
    # except :
        # print("+++++++++++++++++++++")
        # dialog = driver.find_element(By.XPATH,"//div[@class='artdeco-modal artdeco-modal--layer-default ']")
        # time.sleep(2)
        # button = driver.find_element(By.XPATH,'//button[@class="fr artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]/span').click()
        # time.sleep(2)
        # count +=1






# inputname=driver.find_elements(By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form/fieldset/div/ul/li/input')
# labelname=driver.find_elements(By.XPATH,'//div[@id="hoverable-outlet-locations-filter-value"]/div/div/div/form/fieldset/div/ul/li/label/p/span[1')
# # print(labelname)
# for i in range(0,len(inputname)):
#     label=labelname.__getitem__(i)
#     print(label)


# for i in name:
#     try:    
#         search=driver.find_element(By.XPATH,'//div[@id="global-nav-typeahead"]/input[1]')
#         search.send_keys(i)
#         search.send_keys(Keys.ENTER)
#     except:
#         pass

# search=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@id="global-nav-typeahead"]/input[1]')))
# search.send_keys('surat')
# time.sleep(2)
# search.send_keys(Keys.ENTER)
# time.sleep(10)
# company=driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul[1]/li[1]/button')
# # company=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="search-reusables__filter-list"]')))
# action.move_to_element(company).perform()
# company.click()
# time.sleep(2)

# peopledata=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light"]')))
# print(len(peopledata))
# name=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]')
# print(name)
# for i in range(0,len(peopledata)):
#     name=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]')
#     print(name)


time.sleep(15)
driver.quit()




#---------

# home_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//header[@id="global-nav"]/div/a/div/div/li-icon'))).click()
# time.sleep(5) 

# driver.refresh()
# time.sleep(5)
# for u in range(1):
#     driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)
#     time.sleep(5)

# like_buttons = driver.find_elements(By.XPATH, "//div[@class='social-details-social-activity update-v2-social-activity']/div[2]/span/button[1]")
# comment_buttons = driver.find_elements(By.XPATH, "//div[@class='social-details-social-activity update-v2-social-activity']/div[2]/span/following-sibling::span[1]/span/div/button")

# for l_button in like_buttons: 
#     driver.execute_script("arguments[0].scrollIntoView();", l_button)
#     time.sleep(2)

# for c_button in comment_buttons:
#         driver.execute_script("arguments[0].click();", c_button)
#         time.sleep(3)
    
# time.sleep(5)

# comment_write = driver.find_elements(By.XPATH, "//div[@class='social-details-social-activity update-v2-social-activity']/div[3]/div/div/following-sibling::div/form/div/div/div/div/div/following-sibling::div/div/div/div[1]")
# print(len(comment_write))

# for likes, comment_writer in zip(like_buttons, comment_write):
#     like = likes.get_attribute('aria-pressed')

#     like_for_post = random.choice([True, True, True, False, False])
#     comment_for_post = random.choice([True, True, True, False, False])
#     if like_for_post == True:
#         if like == 'false':
#             driver.execute_script("arguments[0].click();", likes)
#             print("Clicked")
#             time.sleep(3)
#     if comment_for_post == True:
#         driver.execute_script("arguments[0].click();", comment_writer)
#         comment_writer.send_keys("Great!!!!!")
#         time.sleep(3)
#         comment_post_button = driver.find_element(By.XPATH, "//div[@class='social-details-social-activity update-v2-social-activity']/div[3]/div/div/following-sibling::div/form/div[2]/button").click()
#         time.sleep(3)

#     time.sleep(3)


#-----------