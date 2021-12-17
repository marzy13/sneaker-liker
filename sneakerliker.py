
#This script that I wrote basically runs instagram and likes the first five pictures based on the hashtag that the person has entered.
from selenium import webdriver #To run the functions of this script, I had to import the selenium library
from selenium.webdriver.common.keys import Keys #Importing keys will help me to interact with the layout of the wesbite.
import time #This will help me with setting up a specific amount of time for which the function will run
def login(browser):
    browser.get("https://www.instagram.com/") #This fetches the link by using the browser
    time.sleep(5) #This will keep this page open for five seconds before moving to the next page
    username = browser.find_element_by_css_selector("[name='username']")#This function will help me to find the boxes where you enter the login details, this is for the username
    password = browser.find_element_by_css_selector("[name='password']")#This is for the password
    username.send_keys("piccheck13")#This enters the username #You can use this account to test the program
    password.send_keys("cps109")#This enters the password
    time.sleep(5)

def taggy_tag(browser,url):
    sleepy_time = 5 #This will keep this page open for five seconds
    browser.get(url) #This will fetch the url of the picture being selected by the program
    time.sleep(5)
    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")#This will locate the picutre. For this to work, it will look at the element where the picture is stored is defined by css class.
    like_count = 0#This will tell the number of pictures liked
    for a in pictures: #This uses a for loop to run through each picture
        if like_count>=5: #This will ensure that only five pictures were liked. After the fifth picture, the loop will break.
            break
        a.click() #This will click on the picture
        time.sleep(sleepy_time)#Will open the page for five seconds
        heart = browser.find_element_by_css_selector("[aria-label='Like']") #This will find the like button by the same method how the picture is found.
        heart.click()#This will click on the heart icon
        close = browser.find_element_by_css_selector("[aria-label='Close']") #After liking the picture, it will close the window and move to the next picture
        close.click()#This clicks on the close icon
        like_count = like_count+1#This will add the picture to the like_count

def main():
    browser = webdriver.Chrome()#This opens the browser, webdriver needs to be installed for your browser
    login(browser) #uses the def browser to run

    tags=[      #This is the main place where you enter your hashtags for your picture to be liked
        "Jordans",
        "Sneakers",
        "Yeezys",
        "Offwhite",
        "Supreme",
        "Vlone",
        "Nike",
        "Jordan1",
        "TS1",
        "TS4",
        "TS6",
        "Yeezy 350",
        "Airmax",
        "Bape"
    ]
    while True: #This while loop will ensure that the website gets redirected to the hashtag.
        for i in tags:
            taggy_tag(browser, f"https://www.instagram.com/explore/tags/{i}")
        time.sleep(1800) #This function will tell you that for how long will this script run, in this case, it will run for 1800 seconds (every 30 minutes)

main()

#NOTE- webdriver for the browser needs to be installed

