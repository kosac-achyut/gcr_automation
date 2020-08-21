from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def login(username,passwordStr,browser):
	
	browser.get(('https://stackoverflow.com/'));

	login = browser.find_element_by_class_name('login-link');
	login.click();

	google_button = browser.find_element_by_class_name('s-btn__google')
	google_button.click();

	browser.implicitly_wait(10)

	name = browser.find_element_by_id('identifierId')
	name.send_keys(username)


	nextButton = browser.find_element_by_class_name('VfPpkd-LgbsSe')
	nextButton.click()


	password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
	password.send_keys(passwordStr)


	browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click(); 

def gcr_login2(class_name,browser):

	print(class_name)

	browser.get(('https://meet.google.com/'));

	browser.find_element_by_class_name('ox9SMb ').click()

	join_class_name = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')))
	join_class_name.send_keys(class_name)

	browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span').click()
	browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()


def gcr_login(class_name,browser):
	
	print(class_name)
	
	browser.get(('https://meet.google.com/'));

	myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/input')))

	myElem.send_keys(class_name)




	browser.find_element_by_xpath('//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/a/button').click()

	browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()

#def class_join_fun(browser):

	#browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()



	# browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span').click()


	# browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea').send_keys("Good Morning")


	# browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[2]/div[3]/div/span/span').click()





	# browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span').click();





#<input type="password" class="whsOnd zHQkBf"

# username = "as8232@srmist.edu.in"
# passwordStr = "This_is_my@Account12"
# class_name = "dpj7nfbrzx"


# gcr_automate(class_name,username,passwordStr)






