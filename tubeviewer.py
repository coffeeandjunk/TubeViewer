import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint, sample
from videos import videos

chromedriver = './drivers/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

# driver = webdriver.Chrome("./drivers/chromedriver")
# driver.implicitly_wait(10)
# driver.maximize_window()

print("TubeViewer has started")

def job():

    try:
        view = 0
        current_video = sample(videos, 1)[0]
        print("Viewing ", current_video)
        driver.get(current_video)

        while(view < randint(1, 5)):
            time.sleep(5)
            view = view + 1
            print(view, " view(s)")
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')

    finally:
        print("Sleeping...")
        time.sleep(10)
        print("TubeViewer is awake")
        # driver.quit()

# schedule.every(randint(7, 17)).minutes.do(job)
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
