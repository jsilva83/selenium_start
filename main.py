from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = '/Users/jorgesilva/Chromedriver/chromedriver'
a_url = 'https://www.amazon.es/Apple-MacBook-16-pulgadas-diez-n%C3%BAcleos-diecis%C3%A9is-n%C3%BAcleos/dp/B09JR31B9R/' \
        'ref=sr_1_3_sspa?crid=1CAJVYQ14QKSR&keywords=macbook+pro&qid=1644049340&sprefix=mac%2Caps%2C353&sr=8-3-spons' \
        '&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySTFLRFo1M1JYSjhSJmVuY3J5cHRlZElkPUEwODE2NDU5MVVaMDlTNVJYUTIxRyZlbm' \
        'NyeXB0ZWRBZElkPUEwOTAxMTc0M0YwMlM3M0RTWkVWVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdEx' \
        'vZ0NsaWNrPXRydWU='

# Create a driver to manage the Chrome browser.
a_driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# Load a URL page into the browser window and tab.
a_driver.get(url=a_url)
# Find the information from the web page based in the XPATH of the element in the web page.
price = a_driver.find_element(
    By.XPATH,
    '/html/body/div[4]/div[2]/div[3]/div[10]/div[14]/div[1]/div[1]/span[2]/span[2]/span[1]')
# Print the text of the selected HTML tag element.
print(price.text)
# Get an attribute of the HTML tag.
print(price.get_attribute('class'))
# Create a new browser tab.
a_driver.execute_script("window.open('');")
# Navigate to the new created tab managed by the window_handles list.
a_driver.switch_to.window(a_driver.window_handles[1])
# Open the URL page in the current tab.
a_driver.get(url='https://www.python.org')
# Get information from the HTML tag with parent class 'documentation-widget' and tag element type 'a'.
documentation_link = a_driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
print(documentation_link.text)
# Switch back to the first tab.
a_driver.switch_to.window(a_driver.window_handles[0])
# Close current tab.
a_driver.close()
# Quit the browser.
a_driver.quit()

