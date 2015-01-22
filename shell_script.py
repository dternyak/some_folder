from selenium import webdriver
import time
import os
import requests
from bs4 import BeautifulSoup

my_path = "/Users/danielternyak/desktop"
actual_file = os.path.join(my_path, "playlist.txt")

with open(actual_file, "r") as my_input:
    for line in my_input:
        print(line)
        url = "https://www.youtube.com/results?search_query=" + str(line)
        selector = "#results .yt-lockup-title a"
        html = requests.get(url).text
        soup = BeautifulSoup(html)
        results = soup.select(selector)
        variable = results[1].attrs['href']
        ID = variable[9:]
        driver = webdriver.Chrome()
        driver.get("http://www.youtube-mp3.org/?e=t_exp&r=true#v=" + ID)
        time.sleep(5)
        elem = driver.find_element_by_link_text('Download')
        elem.click()
        time.sleep(30)      
        driver.close()
