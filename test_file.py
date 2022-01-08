import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
import string
import sys
import os
import bs4
import requests

f = open('scrape.txt','r')
soup = bs4.BeautifulSoup(f,'lxml')
f.close()

title = soup.select('.lister-item-header')
picture = soup.select('.loadlate')
#print(picture[0]['loadlate'])
#print (title[0].find('a').contents[0])
#imdb = title[0].find('a')
#print('https://www.imdb.com'+imdb['href'])
for item in title:
    i = 0
    print(item.find('a').contents[0])
    print(picture[i]['loadlate'])
    imdb = item.find('a')
    print('https://www.imdb.com'+imdb['href'])

