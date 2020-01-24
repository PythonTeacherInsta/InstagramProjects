"""
        Python script for a selfmade Webbrowser
                    @python_teacher
"""

import webbrowser
from tkinter import *

# defining our window
window = Tk()
window.title("Browser")
window.geometry("200x80")

# methods to open the pages
def instagram():
    webbrowser.open("http://instagram.com", new=2)

def google():
    webbrowser.open("http://google.com", new=2)

def youtube():
    webbrowser.open("http://youtube.com", new=2)

def facebook():
    webbrowser.open("http://facebook.com", new=2)

# creating buttons to open the pages
instaButton = Button(window, text="Instagram", command=instagram)
instaButton.grid(row=1, column=0, padx=10)

googleButton = Button(window, text="Google", command=google)
googleButton.grid(row=1, column=1, padx=10)

youtubeButton = Button(window, text="Youtube", command=youtube)
youtubeButton.grid(row=2, column=0, padx=10)

facebookButton = Button(window, text="Facebook", command=facebook)
facebookButton.grid(row=2, column=1, padx=10)

window.mainloop()
