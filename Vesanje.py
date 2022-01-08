from tkinter import *
from PIL import Image, ImageTk
import random
import sys
import os
import bs4
import requests
import webbrowser

prva_greska = Image.open("prva greska.png")
druga_greska = Image.open("druga greska.png")
treca_greska = Image.open("treca greska.png")
cetvrta_greska = Image.open("cetvrta greska.png")
peta_greska = Image.open("peta greska.png")
sesta_greska = Image.open("sesta greska.png")
kraj = Image.open("kraj.png")

greske = {1:prva_greska, 2:druga_greska, 3:treca_greska, 4:cetvrta_greska, 5:peta_greska, 6:sesta_greska, 7:kraj}

titles = []
pictures = []
imdb_links = []

action = "https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=6AMK575RVRXPDJPXYFCK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1"
adventure = "https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=6AMK575RVRXPDJPXYFCK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2"
comedy = "https://www.imdb.com/search/title/?genres=comedy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=6AMK575RVRXPDJPXYFCK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_5"
drama = "https://www.imdb.com/search/title/?genres=drama&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=6AMK575RVRXPDJPXYFCK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_7"
horror = "https://www.imdb.com/search/title/?genres=horror&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=PNVVBPMXD7B04F1VJ7W2&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_12"
sci_fi = "https://www.imdb.com/search/title/?genres=sci_fi&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=PNVVBPMXD7B04F1VJ7W2&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_17"
crime = "https://www.imdb.com/search/title/?genres=crime&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=PNVVBPMXD7B04F1VJ7W2&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_6"

f = open('scrape.txt','r')
soup = bs4.BeautifulSoup(f,'lxml')
f.close()

title = soup.select('.lister-item-header')
picture = soup.select('.loadlate')
i = 0
for item in title:

    titles.append(item.find('a').contents[0])
    pictures.append(picture[i]['loadlate'])
    imdb = item.find('a')
    imdb_links.append('https://www.imdb.com'+imdb['href'])
    i += 1

def scraper(link):

    headers = {"Accept-Language": "en-US,en;q=0.5"}
    res = requests.get(link,headers=headers)
    f = open('scrape.txt','w')
    f.write(res.text)
    f.close()


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def win():

    global img
    global link

    novi_prozor = Toplevel(prozor)
    novi_prozor.title("Pobeda")
    novi_prozor.geometry("450x450")
    Button(novi_prozor, text="Restart", command=restart).pack()
    Label(novi_prozor,text ="Cestitamo, pobedili ste !!!").pack()
    linked_resenje = Label(novi_prozor,text = resenje, font = "Calibri 16",fg="blue", cursor="hand2")
    linked_resenje.pack()
    linked_resenje.bind("<Button-1>", lambda e: callback(link))
    render = ImageTk.PhotoImage(img)
    img = Label(novi_prozor, image = render,highlightthickness = 0, borderwidth = 0)
    img.image = render
    img.place(relx=0.4,rely=0.3)

def callback(url):
    webbrowser.open_new(url)

def lose():

    global img
    global link

    novi_prozor = Toplevel(prozor)
    novi_prozor.title("Poraz")
    novi_prozor.geometry("450x450")
    Button(novi_prozor, text="Restart", command=restart).pack()
    Label(novi_prozor,text ="Izgubili ste").pack()
    linked_resenje = Label(novi_prozor,text = resenje, font = "Calibri 16",fg="blue", cursor="hand2")
    linked_resenje.pack()
    linked_resenje.bind("<Button-1>", lambda e: callback(link))
    render = ImageTk.PhotoImage(img)
    img = Label(novi_prozor, image = render,highlightthickness = 0, borderwidth = 0)
    img.image = render
    img.place(relx=0.4,rely=0.3)

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def refresh_movies():

    novi_prozor = Toplevel(prozor)
    novi_prozor.title("Change Movie Genre")
    novi_prozor.geometry("1200x200")
    Label(novi_prozor, font = "Calibri 26", text = "Choose Movie Genre", justify = CENTER).pack()
    Action = Button(novi_prozor, text = "Action", fg = 'black', bg = 'light gray', command = lambda:[scraper(action),novi_prozor.destroy(),restart()])
    Action.place(relx = 0.100, rely = 0.60, height = 40, width = 110)
    Adventure = Button(novi_prozor, text = "Adventure", fg = 'black', bg = 'light gray', command = lambda:[scraper(adventure),novi_prozor.destroy(),restart()])
    Adventure.place(relx = 0.200, rely = 0.60, height = 40, width = 110)
    Comedy = Button(novi_prozor, text = "Comedy", fg = 'black', bg = 'light gray', command = lambda:[scraper(comedy),novi_prozor.destroy(),restart()])
    Comedy.place(relx = 0.300, rely = 0.60, height = 40, width = 110)
    Drama = Button(novi_prozor, text = "Drama", fg = 'black', bg = 'light gray', command = lambda:[scraper(drama),novi_prozor.destroy(),restart()])
    Drama.place(relx = 0.400, rely = 0.60, height = 40, width = 110)
    Horror = Button(novi_prozor, text = "Horror", fg = 'black', bg = 'light gray', command = lambda:[scraper(horror),novi_prozor.destroy(),restart()])
    Horror.place(relx = 0.500, rely = 0.60, height = 40, width = 110)
    Sci_Fi = Button(novi_prozor, text = "Sci_Fi", fg = 'black', bg = 'light gray', command = lambda:[scraper(sci_fi),novi_prozor.destroy(),restart()])
    Sci_Fi.place(relx = 0.600, rely = 0.60, height = 40, width = 110)
    Crime = Button(novi_prozor, text = "Crime", fg = 'black', bg = 'light gray', command = lambda:[scraper(crime),novi_prozor.destroy(),restart()])
    Crime.place(relx = 0.700, rely = 0.60, height = 40, width = 110)



resenje = random.choice(titles)
link = imdb_links[titles.index(resenje)]
img_link = requests.get(pictures[titles.index(resenje)])
img_file = open(resenje + '.jpg','wb')
img_file.write(img_link.content)
img_file.close()
img = Image.open(resenje + '.jpg')

A = []
B = []


for a in resenje:
    A.append(a)
    if a.isalpha():
        B.append("_")
    else:
        B.append(a)

listToStr = ' '.join(map(str, B))


def greska(slika):
    render = ImageTk.PhotoImage(slika)
    img = Label(prozor, image = render,highlightthickness = 0, borderwidth = 0)
    img.image = render
    img.place(relx=0.8, rely=0.1)

num = 0

def enter(e):
    global listToStr
    global num
    global my_label
    k = 0
    provera_greske = ''.join(map(str, B))
    
    pokusaj = S.get()
    for slovo in A:
        if slovo.lower() == pokusaj:
            B.pop(k)
            B.insert(k,slovo)
            k += 1
        else:
            k += 1
    S.set('')
    listToStr = ' '.join(map(str, B))
    my_label.config(text = listToStr)
    if provera_greske == ''.join(map(str, B)):
        num += 1
    if num != 0:
        greska(greske[num])
    if num == 7:
        lose()
    if A == B:
        win()

def enter1():
    global listToStr
    global num
    global my_label
    k = 0
    provera_greske = ''.join(map(str, B))
    
    pokusaj = S.get()
    for slovo in A:
        if slovo.lower() == pokusaj:
            B.pop(k)
            B.insert(k,slovo)
            k += 1
        else:
            k += 1
    S.set('')
    listToStr = ' '.join(map(str, B))
    my_label.config(text = listToStr)
    if provera_greske == ''.join(map(str, B)):
        num += 1
    if num != 0:
        greska(greske[num])
    if num == 7:
        lose()
    if A == B:
        win()

#Driver code
if __name__ == "__main__":

#kreiranje prozora
    prozor = Tk()
    prozor.resizable(False, False)
    #postavljanje boje pozadine prozora
    prozor.configure(background = "OliveDrab2")

    #postavljanje teksta naslova prozora
    prozor.title("Vesanje")

    #postavljanje dimenzija prozora
    prozor.geometry("1280x720")

    #StringVar() je klasa varijabli
    #kreiranje objekta iz klase StringVar()
    S = StringVar()  #!!!

    #kreiranje textbox-a za prikaz izraza
    expression_field = Entry(prozor, textvariable = S, font = "Calibri 36", justify = CENTER)
    expression_field.bind('<Return>', enter)
    #grid metoda se koristi za postavljanje widgeta na svoje pozicije u prozoru
    expression_field.place(relx = 0.8, rely = 0.8, anchor = SE, height = 60, width = 55)
    if len(resenje) < 20:
        my_font = 'Calibri 26'
    elif len(resenje) < 25:
        my_font = 'Calibri 24'
    elif len(resenje) < 30:
        my_font = 'Calibri 22'
    elif len(resenje) < 35:
        my_font = 'Calibri 20'
    elif len(resenje) < 40:
        my_font = 'Calibri 18'
    elif len(resenje) < 45:
        my_font = 'Calibri 16'
    elif len(resenje) < 50:
        my_font = 'Calibri 14'
    else:
        my_font = 'Calibri 12'
    my_label = Label(prozor, font = my_font, text = listToStr)
    my_label.place(relx = 0.1, rely = 0.1, anchor = NW, height = 200)
    my_label.configure(bg = "OliveDrab2", highlightthickness = 0, borderwidth = 0)

    Enter = Button(prozor, text = "Enter", fg = 'black', bg = 'light gray', command = enter1)
    Enter.place(relx = 0.755, rely = 0.81, height = 40, width = 70)

    Refresh = Button(prozor, text = "Refresh Movies", fg = 'black', bg = 'light gray', command = refresh_movies)
    Refresh.place(relx = 0.150, rely = 0.81, height = 50, width = 120)


#pokreni graficki interfejs
    prozor.mainloop()

os.remove(resenje + '.jpg')