from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import threading

############################################################

emailname='frogbot'
emailpass='fr0g#b0t'
FirstName='frog'
LastName='bot'
frogidsy='fg'
frogid='1'

############################################################
def signupemail(emailname,emailpass,FirstName,LastName,itbrowser):#make email for bot
    browser=itbrowser
    browser.get('https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1610394737&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3da63727b1-cf50-1e4c-37f8-23b0c47d1a78&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=b73ca81378ee4a97823eea7319889fdd')
    sleep(1)
    emailuserbox=browser.find_element_by_xpath('//*[@id="MemberName"]')
    emailuserbox.send_keys(emailname+frogidsy+frogid)
    sleep(1)
    nextbox=browser.find_element_by_xpath('//*[@id="iSignupAction"]')
    nextbox.click()
    sleep(1)
    emailpassbox=browser.find_element_by_xpath('//*[@id="PasswordInput"]')
    emailpassbox.send_keys(emailpass)
    sleep(1)
    nextbox=browser.find_element_by_xpath('//*[@id="iSignupAction"]')
    nextbox.click()
    sleep(1)
    emailFirstNamebox=browser.find_element_by_xpath('//*[@id="FirstName"]')
    emailFirstNamebox.send_keys(FirstName)
    emailLastNamebox=browser.find_element_by_xpath('//*[@id="LastName"]')
    emailLastNamebox.send_keys(LastName)
    sleep(1)
    nextbox=browser.find_element_by_xpath('//*[@id="iSignupAction"]')
    nextbox.click()
    #sleep(1)
    #listbox=browser.find_element_by_xpath('//*[@id="Country"]')
    #listbox.sendKeys(Keys.DOWN)
    #listbox.click()
    sleep(1)
    listbox=browser.find_element_by_xpath('//*[@id="BirthMonth"]')
    listbox = Select(listbox)
    listbox.select_by_index(12)
    listbox=browser.find_element_by_xpath('//*[@id="BirthDay"]')
    listbox = Select(listbox)
    listbox.select_by_index(12)
    listbox=browser.find_element_by_xpath('//*[@id="BirthYear"]')
    listbox = Select(listbox)
    listbox.select_by_index(26)
    nextbox=browser.find_element_by_xpath('//*[@id="iSignupAction"]')
    nextbox.click()
    ###########################################################
    sleep(14)
    nextbox=browser.find_elements_by_xpath('/html/body/div[4]/span/a[2]/span')
    print("body found")
#    action = ActionChains(browser)
#    action.key_down(Keys.TAB)
#    action.key_up(Keys.TAB)
#    action.click()
    print("finish email")
###########################################################
def getconfrmationcode():
    CODE="123456789"
    return CODE
###########################################################    
def signupinstagram(emailname,emailpass,FirstName,LastName,frogid,itbrowser):
    browser=itbrowser
    #######--1
    browser.get('https://www.instagram.com/accounts/emailsignup/')
    sleep(1)
    instaemailuserbox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[3]/div/label/input')
    instaemailuserbox.send_keys(emailname+'@hotmail.com')
    instafullnamebox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[4]/div/label/input')
    instafullnamebox.send_keys(FirstName+LastName)
    instausernamebox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/label/input')
    instausernamebox.send_keys(FirstName+frogidsy+frogid)
    instapassbox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[6]/div/label/input')
    instapassbox.send_keys(emailpass)
    nextbox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[7]/div/button')
    nextbox.click()
    #######--2
    sleep(1)
    listbox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select')
    listbox = Select(listbox)
    listbox.select_by_index(5)
    listbox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select')
    listbox = Select(listbox)
    listbox.select_by_index(5)
    listbox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
    listbox = Select(listbox)
    listbox.select_by_index(26)
    loginbutton=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
    loginbutton.click()
    #######--3
    sleep(3)
    instaconfrmationbox=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')
    instaconfrmationbox.send_keys(getconfrmationcode())
    instanextbutton=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
    instanextbutton.click()
    #######--4
    sleep(1)
    print('finish instagram')
###########################################################    
def signininstagram(emailname,emailpass,itbrowser):
    browser=itbrowser
    browser.get('https://www.instagram.com/')
    sleep(1)
    loginuserbox=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    loginuserbox.send_keys(emailname)
    sleep(1)
    loginpassbox=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    loginpassbox.send_keys(emailpass)
    sleep(1)
    loginbutton=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    loginbutton.click()
###########################################################
#################||||main||||##############################

#signupemail(emailname,emailpass,FirstName,LastName,botbrowser1)
#signupinstagram(emailname,emailpass,FirstName,LastName,frogid,botbrowser2)
#newtabe()

def worker():
    webbrowser = webdriver.Firefox()
    signupemail(emailname,emailpass,FirstName,LastName,webbrowser)
    #signupinstagram(emailname,emailpass,FirstName,LastName,frogid,webbrowser)
    #signininstagram(emailname,emailpass,webbrowser)

def webthread(webbrowserumber):
    threads = []
    for i in range(webbrowserumber):
        t = threading.Thread(target=worker, args=())
        print(t)
        threads.append(t)
        t.start()

webthread(1)
#################||||main||||##############################
###########################################################
def tabsthread():
    threadstabs = []
    tab=0
    for ii in range(tabs, 0, -1):
        tt = threading.Thread(target=newtabe, args=(tab,webbrowser))
        threadstabs.append(tt)
        tt.start()
        tab=tab+1
        sleep(15)
###########################################################
tabs=0
def newtabe(tabs,itbrowser):#make new tabe
    browser=itbrowser
    browser.execute_script('''window.open("","_blank");''')
    browser.switch_to.window(browser.window_handles[tabs])
    print(tabs)
    signupinstagram(emailname,emailpass,FirstName,LastName,frogid,browser)
###########################################################

#browser.close()
#import requests
#web = requests.get('https://www.instagram.com/accounts/emailsignup/')
#print(web)

