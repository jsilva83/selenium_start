from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = '/Users/jorgesilva/Chromedriver/chromedriver'
a_url = 'https://www.python.org/'

a_driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# Load a URL page into the browser window and tab.
a_driver.get(url=a_url)
# Find the information from the web page based in the XPATH of the element in the web page.
output = {}
for a_n in range(5):
    event_date = a_driver.find_element(
        By.XPATH,
        f'/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{a_n + 1}]/time')
    # /html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[2]/time
    event_location = a_driver.find_element(
        By.XPATH,
        f'/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{a_n + 1}]/a')
    # /html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[2]/a
    output[a_n] = {'time': event_date.text, 'name': event_location.text}
print(output)
a_driver.quit()