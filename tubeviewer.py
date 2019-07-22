import schedule
import time
import datetime
import sys
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint, sample
from videos import videos

import sys
import subprocess

if 'darwin' in sys.platform:
    subprocess.Popen('caffeinate')

def job():

    try:
        chromedriver = './drivers/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--test-type')
        # options.binary_location = "/usr/bin/chromium"

        driver = webdriver.Chrome(executable_path=chromedriver, options=options)
        driver.implicitly_wait(10)
        current_time = datetime.datetime.now().strftime("%X")
        print("[",current_time,"]", " TubeViewer has started")

        current_video = sample(videos, 1)[0]
        driver.get(current_video)
        current_time = datetime.datetime.now().strftime("%X")
        print("[",current_time,"]", "Viewing: ", current_video)

        driver.implicitly_wait(10)
        yt_duration = driver.find_element_by_class_name('ytp-time-duration').text
        # print(yt_duration)
        minutes = yt_duration[:yt_duration.find(":")]
        # print(minutes)
        seconds = yt_duration[-2:]
        # print(seconds)
        duration = (int(minutes) * 60) + int(seconds)
        print("Duration: ", duration, " secs")

        yt_play_btn = driver.find_element_by_class_name('ytp-play-button')
        yt_play_btn.click()
        ytp_mute_btn = driver.find_element_by_class_name('ytp-mute-button')
        ytp_mute_btn.click()

        # time.sleep(10)
        # driver.save_screenshot("screenshot1.png")
        # time.sleep(20)
        # driver.save_screenshot("screenshot2.png")
        # time.sleep(30)
        # driver.save_screenshot("screenshot3.png")

        time.sleep(duration)
        # time.sleep(10)

        # driver.find_element_by_id('logo-icon-container').click()
        # print("Went to YouTube home screen.")
        # time.sleep(randint(120, 240))
        # time.sleep(10)

    finally:
        current_time = datetime.datetime.now().strftime("%X")
        print("[",current_time,"]", "TubeViewer has quit.")
        driver.quit()

schedule.every(randint(3, 7)).minutes.do(job)
# schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
