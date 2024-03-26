from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html') #opens up a new browser each time
 
# This solves the issue with the Popup for those that encounter it:
chrome_browser.implicitly_wait(2)
popup =chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
popup.click()
 
 
 
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')
 
time.sleep(2)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()
 
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I AM EXTRA COOOOL' in output_message.text


show_message_button = chrome_browser.find_element_by_class_name('btn-default') #grabs web element that is a button
print(show_message_button.get_attributes('innerHTML')) #grabs the ineerHTML of the button object

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOooL')

show_message_button.click()

chrome_browser.close() #you have to put it in twice to make sure no bugs keep it open
chrome_browser.close()
chrome_browser.quit() #this will also just quit the browser