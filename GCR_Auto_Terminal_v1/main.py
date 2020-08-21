import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
from datetime import datetime , timedelta
from module import login,gcr_login,gcr_login2,class_join_fun

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1})

dir_path = os.path.dirname(os.path.realpath(__file__))
username = ""
passwordStr = ""
location = '/Users/achyutsaroch/Project/Autologin_for_GCR/project/chromedriver'
browser = webdriver.Chrome(chrome_options=opt,executable_path = location)
browser.get(('file://'+dir_path+'/index.html'))

def main_func(class_name ,sh ,sm ,le,session):
	x=datetime.today();
	y=x.replace(day=x.day,hour=sh,minute=sm,second=0,microsecond=0) + timedelta(days=1)
	delta_t=y-x;
	secs = delta_t.seconds + 1	
	time.sleep(secs)
	print("Enter Automated Message:")
	message = input()	
	print("Login in Class:",class_name,"\n")
	if session == 0:
		login(username,passwordStr,browser)
		gcr_login(class_name,browser)
	else :
		gcr_login2(class_name,browser)
	class_join_fun(browser,message)	
	time.sleep(le*60)
	




list_time = []
print("Good Morning")
print("Username and Password")
username = input();
passwordStr = input();
print("Enter number of class today")
no_of_classes = int(input())
print("Enter Class Name  with start time  in format of 24:00 and length of class in minute")
for i in range(0,no_of_classes):
	list_time.append([])
	name = input();
	list_time[i].append(name);
	x,y = input().split(':')
	list_time[i].append(int(x))
	list_time[i].append(int(y))
	le = int(input())
	list_time[i].append(int(le))	
print("Automation started")
for i in range(0,no_of_classes):
	main_func(list_time[i][0],list_time[i][1],list_time[i][2],list_time[i][3],i)

browser.quit()	
	#time.sleep(secs)








