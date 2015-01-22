from selenium import webdriver
import time
import os
import requests
from bs4 import BeautifulSoup
from tkinter import *
import sys
    
mGui = Tk()
v = StringVar()

# Variable to hold the input
inp = None

E1 = Entry(textvariable = v)
E1.pack(side = RIGHT)

def userinput():
    # Declare 'inp' to be global
    global inp
    a = v.get()
    # Update the variable
    inp = a
    #### begins main downloade
    url = "https://www.youtube.com/results?search_query=" + str(inp)
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


b = Button(mGui, text = 'Submit', command = userinput)
b.pack(side = BOTTOM)


mGui.mainloop()
