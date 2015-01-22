from selenium import webdriver
import time
import os
import requests
from bs4 import BeautifulSoup
from Tkinter import *
import sys
    
mGui = Tk()
v = StringVar()

# Variable to hold the input
inp = None

E1 = Entry(textvariable = v)
E1.pack(side = RIGHT)

def translate_non_alphanumerics(to_translate, translate_to=u''):
	global title_text
	not_letters_or_digits = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'
	translate_table = dict((ord(char), translate_to) for char in not_letters_or_digits)
	title_str_text = to_translate.translate(translate_table)
	title_text = title_str_text

def userinput():
    path_to_auto_add = "/Users/danielternyak/Music/iTunes/iTunes\ Media/Automatically\ Add\ to\ iTunes.localized/"
    
    # Declare 'inp' to be global
    global inp
    a = v.get()
    # Update the variable
    inp = a
    #### begins main download
    url = "https://www.youtube.com/results?search_query=" + str(inp)
    time.sleep(5)
    selector = "#results .yt-lockup-title a"
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    results = soup.select(selector)
    variable = results[1].attrs['href']
    ID = variable[9:]
    driver = webdriver.PhantomJS(executable_path ="/usr/local/bin/phantomjs")
    driver.get("http://www.youtube-mp3.org/?e=t_exp&r=true#v=" + ID)
    driver.implicitly_wait(10)
    elem = driver.find_element_by_link_text('Download')
    elem.click()
    time.sleep(3)
    print "check downloads"
    driver.close()


b = Button(mGui, text = 'Submit', command = userinput)
b.pack(side = BOTTOM)


mGui.mainloop()
