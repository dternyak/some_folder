import urllib
from urlparse import urljoin
import os, sys, subprocess
from Tkinter import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# your path to phantomjs.exe
path_to_phantomjs_exe = "/Library/Python/2.7/site-packages/phantomjs-1.9.8-macosx/bin/phantomjs"    
mGui = Tk()
v = StringVar()

# Variable to hold the input
inp = None

E1 = Entry(textvariable = v)
E1.pack(side = RIGHT)

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def translate_non_alphanumerics(to_translate, translate_to=u''):
	global title_text
	not_letters_or_digits = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'
	translate_table = dict((ord(char), translate_to) for char in not_letters_or_digits)
	title_str_text = to_translate.translate(translate_table)
	title_text = title_str_text

def userinput():
    driver = webdriver.PhantomJS(executable_path= path_to_phantomjs_exe)
    # Declare 'inp' to be global
    global inp
    a = v.get()
    # Update the variable
    inp = str(a).replace(" ", "+")
    #### begins main download
    driver.get("https://www.youtube.com/results?filters=video&lclk=video&search_query=" + inp + "+lyrics")
    
	#find href link within Youtube html, then parse the video id
    links = driver.find_elements(By.CLASS_NAME, "yt-lockup-title")
    link = links[0]
    link = link.get_attribute('innerHTML')
    link = link.split(' ')[1]
    link = link.replace('href="/watch?v=', '')
    link = link.replace('"', '')
    
    driver.get("http://www.youtube-mp3.org/?e=t_exp&r=true#v="+link)
    element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.LINK_TEXT, "Download")))
    
    link = element.get_attribute('href')
    title_element = driver.find_element_by_id("title")
    title_text = title_element.get_attribute('innerHTML')
    title_text = title_text.replace("<b>Title:</b>", "")
    translate_non_alphanumerics(title_text)
    
    # your desired destination path of the downloaded mp3 files
    mp3_download_path = "/Users/jameslemieux/Downloads/my_music/"+title_text+".mp3"
    
    download_directory = mp3_download_path.replace(title_text, '')
    download_directory = download_directory.replace('.mp3', '')
    
    if os.path.exists(mp3_download_path):
        print "already in downloads"
    else:
        urllib.urlretrieve(link, mp3_download_path)
        open_file(mp3_download_path) #adds mp3 to itunes library
    print "check downloads"
    driver.close()


b = Button(mGui, text = 'Submit', command = userinput)
b.pack(side = BOTTOM)


mGui.mainloop()
