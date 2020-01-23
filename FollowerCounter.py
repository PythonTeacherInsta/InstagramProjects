"""
        Python script for a instagram follower counter
                    @python_teacher
"""

# imports
from tkinter import *
import requests
from tkinter.messagebox import showinfo

# defining our window
window = Tk()
window.title("Follower Counter")
window.geometry("200x80")

# method to check instagramm follower
def instagram():
    # Set your Instagram username here
    user = entry.get()
    url = 'https://www.instagram.com/' + user
    r = requests.get(url).text

    start = '"edge_followed_by":{"count":'
    end = '},"followed_by_viewer"'

    follower = r[r.find(start)+len(start):r.rfind(end)]
    showinfo("Follower", user + ": " + follower + " follower")

entry = Entry(window)
entry.grid(row=0, column=0)

button = Button(window, text="Check", command=instagram)
button.grid(row=1, column=0, padx=10)

window.mainloop()