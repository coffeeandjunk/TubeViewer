import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint, sample
from videos import videos

def job():

    try:
        chromedriver = './drivers/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(executable_path=chromedriver, options=options)
        driver.implicitly_wait(10)
        print("TubeViewer has started")

        current_video = sample(videos, 1)[0]
        driver.get(current_video)
        print("Viewing: ", current_video)

        driver.implicitly_wait(10)
        yt_duration = driver.find_element_by_class_name('ytp-time-duration').text
        # print(yt_duration)
        minutes = yt_duration[:yt_duration.find(":")]
        # print(minutes)
        seconds = yt_duration[-2:]
        # print(seconds)
        duration = (int(minutes) * 60) + int(seconds)
        print("Duration: ", duration, " secs")

        time.sleep(duration)
        # time.sleep(10)

        driver.find_element_by_id('logo-icon-container').click()
        print("Went to YouTube home screen.")
        time.sleep(randint(120, 240))
        # time.sleep(10)

    finally:
        print("TubeViewer has quit.")
        driver.quit()

schedule.every(randint(15, 30)).minutes.do(job)
# schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
