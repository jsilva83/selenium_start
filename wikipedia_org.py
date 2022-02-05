from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = '/Users/jorgesilva/Chromedriver/chromedriver'
a_url = 'https://en.wikipedia.org/wiki/Main_Page'


a_driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# Load a URL page into the browser window and tab.
a_driver.get(url=a_url)
number_of_articles_en = a_driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]')
print(number_of_articles_en.text)
number_of_articles_en.click()
# a_driver.back()
a_driver.execute_script("window.history.go(-1)")
all_portals = a_driver.find_element(By.LINK_TEXT, "All portals")
all_portals.click()
a_driver.execute_script("window.history.go(-1)")
search = a_driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/form/div/input[1]')
search.send_keys('Python')
search.send_keys(Keys.ENTER)
zoom = a_driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div/form/div/input[3]')
zoom.click()
a_driver.quit()
