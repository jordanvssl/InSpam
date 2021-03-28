import time, getpass
from termcolor import colored
from art import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colored import fg, bg, attr

#Var
copy = "https://github.com/jordanvssl/InSpam "
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
warn = "%s%sPlease turn off 2FA on your Instagram account !!!  %s" % (
    fg("black"),
    bg("red"),
    attr("reset"),
)
loop = 0
space = " "
erase = "\033[A                                                                                                       \033[A"

tprint("InSpam")
print(colored(copy, "green"))
time.sleep(2)
print(space)
print(warn)
print(space)
# Form
chromedriver = input("Path for chromedriver: ")
print(erase)
username = input("Instagram username: ")
print(erase)
password = getpass.getpass("Enter your password: ")
print(erase)
target = input("Target username: ")
print(erase)
messageNb = int(input("Message Number: "))
print(erase)
SpamText = input("Message (ex:Hello World): ")
print(erase)
delay = int(
    input(
        "This is the time between actions | Good internet connection put 3 | medium 5 | bad 10: "
    )
)
print(erase)
print("Starting, wait...")
print(space)
print("Please do not close the window")
time.sleep(5)

# Get
driver = webdriver.Chrome(chromedriver, options=options)
driver.get("http://www.instagram.com")

time.sleep(delay)
driver.find_element_by_class_name("bIiDR").click()
time.sleep(delay)
driver.find_element_by_name("username").send_keys(username)
time.sleep(2)
driver.find_element_by_name("password").send_keys(password)
time.sleep(2)
driver.find_element_by_class_name("y3zKF").click()
time.sleep(delay)
driver.get("https://www.instagram.com/direct/inbox/")
try:
    driver.find_element_by_class_name("HoLwm").click()
except:
    pass
time.sleep(delay)
driver.find_element_by_class_name("L3NKy").click()
time.sleep(delay)
try:
	driver.find_element_by_class_name("M5V28").send_keys(target)
except:
	print('error, please restart...')
time.sleep(2)
driver.find_element_by_class_name("dCJp8").click()
time.sleep(2)
driver.find_element_by_class_name("rIacr").click()
time.sleep(delay)

# Loop
while loop < messageNb:
    loop += 1
    textarea = driver.find_element_by_xpath("//textarea")
    textarea.send_keys(SpamText)
    textarea.send_keys(Keys.RETURN)
print(space)
print("Success")
driver.close()
exit()
