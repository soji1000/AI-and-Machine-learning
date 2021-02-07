

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/soji/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.walmart.com/account/login?tid=0&returnUrl=%2F")

username = driver.find_element_by_id("email")
username.send_keys("adetunjigbenga37@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("f3K7g7xXEeTB")

login_btn = driver.find_element_by_xpath('//*[@id="sign-in-form"]/button[1]').click()

time.sleep(1)
search = driver.find_element_by_xpath('//*[@id="global-search-input"]')
search.send_keys("ps5 controller")
#time.sleep(2)
search.send_keys(Keys.RETURN)
time.sleep(1)
ps5link = driver.find_element_by_link_text("Sony PlayStation 5 DualSense Wireless Controller")
ps5link.click()

time.sleep(2)
add_to_cart = driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span').click()
time.sleep(3)
checkout_btn = driver.find_element_by_xpath('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]/span').click()
time.sleep(3)
place_order = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button/span').click()

enter_csv = driver.find_element_by_xpath('//*[@id="cvv-confirm"]')
enter_csv.send_keys('940')

