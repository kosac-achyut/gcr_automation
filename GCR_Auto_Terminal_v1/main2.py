from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options




class_name = input();

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })







location = '/Users/achyutsaroch/Project/Autologin_for_GCR/project/chromedriver'
browser = webdriver.Chrome(chrome_options=opt,executable_path = location);

browser.get(('https://stackoverflow.com/'));

login = browser.find_element_by_class_name('login-link');
login.click();

google_button = browser.find_element_by_class_name('s-btn__google')
google_button.click();

username = "as8232@srmist.edu.in"
passwordStr = "This_is_my@Account12"



browser.implicitly_wait(10)

name = browser.find_element_by_id('identifierId')
name.send_keys(username)


nextButton = browser.find_element_by_class_name('VfPpkd-LgbsSe')
nextButton.click()


password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(passwordStr)


browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click();


browser.get(('https://meet.google.com/'));


browser.find_element_by_xpath('//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/input').send_keys(class_name)

browser.find_element_by_xpath('//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/a/button').click()

# browser.implicitly_wait(10)

# browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]').click()

browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()



browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()


browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span').click()


browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea').send_keys("Good Morning")


browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[2]/div[3]/div/span/span').click()





browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span').click();




#<input type="password" class="whsOnd zHQkBf"






