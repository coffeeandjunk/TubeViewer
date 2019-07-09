import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = './drivers/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

# driver = webdriver.Chrome("./drivers/chromedriver")
driver.implicitly_wait(30)
# driver.maximize_window()

try:
    view = 0
    print("YT Viewer has started")
    while( view < 100):
        driver.get("https://youtu.be/V7sde1A0mzE")
        time.sleep(474)
        view = view + 1
        print(view, " view(s)")
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')

finally:
    driver.quit()
