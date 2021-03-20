from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# *************** STEP 1 ****************


# Starting with Login Page

#declared a variable driver and used it to store a chrome driver
# ChromeDriverManager().install() fetches the latest chrome driver binaries and installs
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.instagram.com/') 
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds


# *************** STEP 2 ****************

# now we are going to automate the login process:
# assign your login cridentiatl
email = "rohit2000ojha@gmail.com"
passward = "akash2001"

# *************** STEP 3 ****************

# XPaths will be used here to select the element with which our automation script should interact

emailField = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')

passwordField = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')

loginButton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')

# *************** STEP 4 ****************

# connecting field with there data (email -> emailFiled and so on)
# send_keys() method to stimulate the process of writing something in a TextField
# The click() method used in the loginButton is used to stimulate the process of clicking a button!
emailField.send_keys(email)
passwordField.send_keys(passward)

time.sleep(1)

loginButton.click()

# *************** STEP 5 ****************

# Sending tweet mssg, just repeating same step for tweet field and send button

tweet = "Hello Everyone! This is a tweet that I am sending from a selenium automated script written in Python ( It feels really awesome (: ) ."

tweetInputField = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
tweetInputField.send_keys(tweet)

tweetButton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
time.sleep(1)
#tweetButton.click() //un-comment if you want to send mssg