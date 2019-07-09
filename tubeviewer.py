import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint, sample
from videos import videos

chromedriver = './drivers/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')

# driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

driver = webdriver.Chrome("./drivers/chromedriver")
driver.implicitly_wait(10)
# driver.maximize_window()

print("TubeViewer has started")

def job():

    try:
        view = 0
        current_video = sample(videos, 1)[0]
        print("Viewing: ", current_video)
        driver.get(current_video)
        driver.implicitly_wait(10)
        yt_duration = driver.find_element_by_class_name('ytp-time-duration').text
        # print(yt_duration)
        minutes = yt_duration[:yt_duration.find(":")]
        # print(minutes)
        seconds = yt_duration[-2:]
        # print(seconds)
        duration = (int(minutes) * 60) + int(seconds)
        print("Duration: ", duration, " secs")

        while(view < randint(1, 3)):
        # while(view < 5):
            time.sleep(duration)
            # time.sleep(5)
            view = view + 1
            print(view, " view(s)")
            driver.refresh()

    finally:
        driver.find_element_by_id('logo-icon-container').click()
        print("Went to YouTube home screen. Now sleeping...")
        time.sleep(5)
        # time.sleep(randint(10, 25))
        print("TubeViewer is awake")
        # driver.quit()

# schedule.every(randint(7, 17)).minutes.do(job)
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
