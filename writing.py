from tkinter import *
from PIL import Image, ImageTk
import random
import sys
import os
import bs4
import requests
import webbrowser
import time

prozor = Tk()
def list_frame(slika):
    file = Image.open(slika)
    frameCnt = file.n_frames
    frames = [PhotoImage(file=slika,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    return frames
prva_greska = list_frame("prva greska.gif")
druga_greska = list_frame("druga greska.gif")
treca_greska = list_frame("treca greska.gif")
cetvrta_greska = list_frame("cetvrta greska.gif")
peta_greska = list_frame("peta greska.gif")
sesta_greska = list_frame("sesta greska.gif")
kraj = list_frame("kraj.gif")
greske = {1:prva_greska, 2:druga_greska, 3:treca_greska, 4:cetvrta_greska, 5:peta_greska, 6:sesta_greska, 7:kraj}

with open('writing.dat', 'w') as f:
    f.write(json.dumps(prva_greska))

# file = open("druga greska.dat", "w")
# file.write(druga_greska)
# file.close()

# file = open("treca greska.dat", "w")
# file.write(treca_greska)
# file.close()

# file = open("cetvrta greska.dat", "w")
# file.write(cetvrta_greska)
# file.close()

# file = open("peta greska.dat", "w")
# file.write(peta_greska)
# file.close()

# file = open("sesta greska.dat", "w")
# file.write(sesta_greska)
# file.close()

# file = open("kraj.dat", "w")
# file.write(kraj)
# file.close()
