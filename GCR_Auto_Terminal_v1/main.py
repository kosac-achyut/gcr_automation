from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#song_name = input()

location = '/Users/achyutsaroch/Project/Autologin_for_GCR/project/chromedriver'

search = song_name
#passwordStr = 'Achyutsa1234.com'

browser = webdriver.Chrome(location)
browser.get(('https://www.youtube.com/'))


song = browser.find_element_by_tag_name('input')
song.send_keys(search)

click_search = browser.find_element_by_id('search-icon-legacy')
click_search.click()


browser.implicitly_wait(10)

click_song = browser.find_element_by_id('video-title')
click_song.click()
 
# signInButton = browser.find_element_by_id('signIn')
# signInButton.click()


#<div class="VfPpkd-RLmnJb"></div>
