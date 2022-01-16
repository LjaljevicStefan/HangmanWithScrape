from tkinter import Toplevel, PhotoImage, Button, Label, StringVar, Tk, Entry, CENTER, SE, NW, NE
from PIL import Image, ImageTk
import random
import os
import bs4
import requests
import webbrowser
import winsound
from winsound import PlaySound
# Lists for storing scraped data
titles = []
pictures = []
imdb_links = []

# Links for scraping
action = "https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=6AMK575RVRXPDJPXYFCK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1"
adventure = "https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=6AMK575RVRXPDJPXYFCK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2"
comedy = "https://www.imdb.com/search/title/?genres=comedy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=6AMK575RVRXPDJPXYFCK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_5"
drama = "https://www.imdb.com/search/title/?genres=drama&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=6AMK575RVRXPDJPXYFCK&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_7"
horror = "https://www.imdb.com/search/title/?genres=horror&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=PNVVBPMXD7B04F1VJ7W2&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_12"
sci_fi = "https://www.imdb.com/search/title/?genres=sci_fi&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=PNVVBPMXD7B04F1VJ7W2&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_17"
crime = "https://www.imdb.com/search/title/?genres=crime&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=PNVVBPMXD7B04F1VJ7W2&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_6"

# Sounds for the game
correct = lambda: PlaySound('Sounds/correct.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
wrong = lambda: PlaySound('Sounds/wrong.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
winner = lambda: PlaySound('Sounds/win.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
loser = lambda: PlaySound('Sounds/lose.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

# On game running, using bs4 module and lxml library to handle html code
f = open('scrape.txt','r')
soup = bs4.BeautifulSoup(f,'lxml')
f.close()

# Getting titles and picture links
title = soup.select('.lister-item-header')
picture = soup.select('.loadlate')
i = 0

for item in title:

    titles.append(item.find('a').contents[0])                   # Appending titles to titles list
    pictures.append(picture[i]['loadlate'])                     # Appending picture links to pictures list
    imdb = item.find('a')                                       # Assigning part of link which is the adress on imbd of actual movie
    imdb_links.append('https://www.imdb.com'+imdb['href'])      # Concatenating imdb site link with previous part of the link and appending full links of the movies to imdb_links list
    i += 1

# On start of program, generate random title from titles list and that title is the solution of hangman
solution = random.choice(titles)
link = imdb_links[titles.index(solution)]                        # Using indexing to get link of the movie, which is shown on the end of the game
img_link = requests.get(pictures[titles.index(solution)])        # Using indexing to get picture link of particular movie title and scraping that image from web page
img_file = open('cover.jpg','wb')
img_file.write(img_link.content)                                 # Writing image in binary to the variable
img_file.close()
img = Image.open('cover.jpg')                                    # Using Image libray to assign actual picture to variable

A = []                                                           # Creating two lists, one for correct letters, and other for guessing
B = []

for a in solution:                                               # Appendig correct letters to list A, and underscores to list B
    A.append(a)
    if a.isalpha():
        B.append("_")
    else:
        B.append(a)

listToStr = ' '.join(map(str, B))

def list_frame(slika):
# Images(GIFs) for hangman, mistakes

    file = Image.open(slika)
    frameCnt = file.n_frames
    frames = [PhotoImage(file=slika,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    return frames

def update(ind, frames):
# This recursive function is used for rendering gifs of hangman on root window

    global window, label

    if ind >= len(frames):
        return
    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    window.after(20, update, ind, frames)

def mistake(frames):
# This function calls update function when the mistake is made

    global window, label

    window.after(0, update, 0, frames)

def scraper(link):                                          # Argument is link of a page with top 50 movies at the moment of desired movie genre
# This function is updating scrate.txt file, when you want to change genre of movies that you want to guess

    headers = {"Accept-Language": "en-US,en;q=0.5"}         # Language for movie titles
    res = requests.get(link,headers=headers)                # Requesting and getting web page from imdb
    f = open('scrape.txt','w')                              
    f.write(res.text)                                       # Writing web page to scrape.txt file
    f.close()

def restart():
# Restart game function

    global window
    window.destroy()
    os.system('python Vesanje.py')

def win_lose(status_title, message, sound):
# Pop-up window when you win with restart button

    global img
    global link

    sound()
    new_window = Toplevel(window)
    new_window.title(status_title)
    new_window.geometry("450x450")
    Button(new_window, text="Restart", command=restart).pack()
    Label(new_window,text = message).pack()
    linked_solution = Label(new_window,text = solution, font = "Calibri 16",fg="blue", cursor="hand2")         # Printing title of the movie
    linked_solution.pack()
    linked_solution.bind("<Button-1>", lambda e: callback(link))                                               # Binding title of movie (linking), and assining function for opening browser and showing movie on imdb
    render = ImageTk.PhotoImage(img)                                                                           # Assining cover picture of the movie to variable
    img.close()
    img_label = Label(new_window, image = render,highlightthickness = 0, borderwidth = 0)                      # Positioning picture in the window
    img_label.image = render
    img_label.place(relx=0.4,rely=0.3)

def callback(url):
# Function for opening browser

    webbrowser.open_new(url)

def refresh_movies():
# Function that is called with Refresh Movies button, it creates new window with several buttons of choice(movie genres)
# Each button is calling scraper function which updates scrape.txt file, function for quiting the game, and function for restarting the game
# Restarting game is required for using updated scrape.txt file and using different movie genre web page for scraping

    new_window = Toplevel(window)
    new_window.title("Change Movie Genre")
    new_window.geometry("1200x200")
    Label(new_window, font = "Calibri 26", text = "Choose Movie Genre", justify = CENTER).pack()

    Action = Button(new_window, text = "Action", fg = 'black', bg = 'light gray', command = lambda:[scraper(action),new_window.destroy(),restart()])
    Action.place(relx = 0.100, rely = 0.60, height = 40, width = 110)

    Adventure = Button(new_window, text = "Adventure", fg = 'black', bg = 'light gray', command = lambda:[scraper(adventure),new_window.destroy(),restart()])
    Adventure.place(relx = 0.200, rely = 0.60, height = 40, width = 110)

    Comedy = Button(new_window, text = "Comedy", fg = 'black', bg = 'light gray', command = lambda:[scraper(comedy),new_window.destroy(),restart()])
    Comedy.place(relx = 0.300, rely = 0.60, height = 40, width = 110)

    Drama = Button(new_window, text = "Drama", fg = 'black', bg = 'light gray', command = lambda:[scraper(drama),new_window.destroy(),restart()])
    Drama.place(relx = 0.400, rely = 0.60, height = 40, width = 110)

    Horror = Button(new_window, text = "Horror", fg = 'black', bg = 'light gray', command = lambda:[scraper(horror),new_window.destroy(),restart()])
    Horror.place(relx = 0.500, rely = 0.60, height = 40, width = 110)

    Sci_Fi = Button(new_window, text = "Sci_Fi", fg = 'black', bg = 'light gray', command = lambda:[scraper(sci_fi),new_window.destroy(),restart()])
    Sci_Fi.place(relx = 0.600, rely = 0.60, height = 40, width = 110)

    Crime = Button(new_window, text = "Crime", fg = 'black', bg = 'light gray', command = lambda:[scraper(crime),new_window.destroy(),restart()])
    Crime.place(relx = 0.700, rely = 0.60, height = 40, width = 110)

num = 0

def entry():
# This function is called when you take letter guess from entry box
    global listToStr
    global num
    global my_label

    k = 0
    check_mistake = ''.join(map(str, B))                               # Concatenating all letters from list B for mistake check
    guess = S.get()                                                    # Assigning letter from entry box to variable(guess)

    for slovo in A:                                                    # Checking if there is a letter match and swaping underscore with correct letter
        if slovo.lower() == guess.lower():
            B.pop(k)
            B.insert(k,slovo)
            k += 1
        else:
            k += 1

    S.set('')                                                          # Clearing entry box for next guess
    listToStr = ' '.join(map(str, B))                                  # Changing text variable for label
    my_label.config(text = listToStr)                                  # Updates text in label and showing your current progress

    if check_mistake == ''.join(map(str, B)):                          # If there is mistake updating counter for dictionary
        num += 1
    if check_mistake != ''.join(map(str, B)):                          # If guess is correct, playing sound for correct letter
        correct()

    elif num != 0:                                                     # If there was a mistake, calling mistake func and render gif image for mistake, and playing sound for wrong guess
        mistake(mistakes[num])
        wrong()

    if num == 7:                                                       # Checking if game is lost
        win_lose("LOSE", "Sorry, YOU LOSE !", loser)

    if A == B:                                                         # Checking if solution is found
        win_lose("WIN ! ! !", "Congratulations, YOU WIN ! ! !", winner)

def enter(e):
    # This function is for calling entry func on key press(Enter)
    entry()
    
def enter1():
    # This function is for calling entry func on button press(Enter)
    entry()

# Driver code
if __name__ == "__main__":

# Creating root window, setting color of background, title, dimension
    window = Tk()
    window.resizable(False, False)
    window.configure(background = "OliveDrab2")
    window.title("Vesanje")
    window.geometry("1400x800")

    # Using list_frame func for mistake gifs and assign each mistake to variable
    first_mistake = list_frame("Images/first mistake.gif")
    second_mistake = list_frame("Images/second mistake.gif")
    third_mistake = list_frame("Images/third mistake.gif")
    fourth_mistake = list_frame("Images/fourth mistake.gif")
    fifth_mistake = list_frame("Images/fifth mistake.gif")
    sixth_mistake = list_frame("Images/sixth mistake.gif")
    last_mistake = list_frame("Images/last mistake.gif")

    # Creating dictionary for mistake variables, to be used as argument in mistake func
    mistakes = {1:first_mistake, 2:second_mistake, 3:third_mistake, 4:fourth_mistake, 5:fifth_mistake, 6:sixth_mistake, 7:last_mistake}

    # Creating object from class StringVar()
    S = StringVar()  #!!!

    # Creating entry box for guess letters
    expression_field = Entry(window, textvariable = S, font = "Calibri 36", justify = CENTER)

    # Binding entry box to press key event func(Enter)
    expression_field.bind('<Return>', enter)

    # Positioning entry box on root window
    expression_field.place(relx = 0.8, rely = 0.8, anchor = SE, height = 60, width = 55)

    # Creating button for getting entry box letter(guess) and positioning
    Enter = Button(window, text = "Enter", fg = 'black', bg = 'light gray', command = enter1)
    Enter.place(relx = 0.755, rely = 0.81, height = 40, width = 70)

    # Adjusting font for various lenght of movie title
    if len(solution) < 20:
        my_font = 'Calibri 26'
    elif len(solution) < 25:
        my_font = 'Calibri 24'
    elif len(solution) < 30:
        my_font = 'Calibri 22'
    elif len(solution) < 35:
        my_font = 'Calibri 20'
    elif len(solution) < 40:
        my_font = 'Calibri 18'
    elif len(solution) < 45:
        my_font = 'Calibri 16'
    elif len(solution) < 50:
        my_font = 'Calibri 14'
    else:
        my_font = 'Calibri 12'
    
    # Creating label for movie title display(guessing label), positioning, setting collor of background
    my_label = Label(window, font = my_font, text = listToStr)
    my_label.place(relx = 0.1, rely = 0.1, anchor = NW, height = 200)
    my_label.configure(bg = "OliveDrab2", highlightthickness = 0, borderwidth = 0)

    # Creating refresh movies button(changing movies database with scraping)
    Refresh = Button(window, text = "Refresh Movies", fg = 'black', bg = 'light gray', command = refresh_movies)
    Refresh.place(relx = 0.150, rely = 0.81, height = 50, width = 120)

    # Positioning label for displaying gif mistakes
    label = Label(window)
    label.place(relx = 0.9, rely = 0.01, anchor = NE)
    label.configure(highlightthickness = 0, borderwidth = 0)

    # Start graphic interface(mainloop)
    window.mainloop()

# Deleting temp files(cover image for movie)
img.close()
os.remove('cover.jpg')