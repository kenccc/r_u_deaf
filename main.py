import pyttsx3
from tkinter import *
import random
from tkinter import messagebox

engine = pyttsx3.init()
vety = [
    "The cat sat",
    "She ran fast",
    "I ate cake",
    "Birds sing",
    "He sleeps now",
    "Dogs bark",
    "The sun shines",
    "Rain falls",
    "We dance",
    "I see you",
    "She laughs loud",
    "He jumps high",
    "Cars drive by",
    "The moon glows",
    "Stars twinkle",
    "Babies cry",
    "Books read",
    "Trees sway",
    "Fish swim",
    "Clouds float",
    "Hats fly",
    "Kids play",
    "Music plays",
    "Doors close",
    "Windows open",
    "Birds chirp",
    "Cats purr",
    "Dogs wag",
    "Waves crash",
    "Bells ring",
    "Horns honk",
    "Lights flicker",
    "Fires burn",
    "Planes fly",
    "Trains chug",
    "Feet tap",
    "Hands clap",
    "Balloons float",
    "Turtles crawl",
    "Rabbits hop",
    "Squirrels scurry",
    "Bugs buzz",
    "Flowers bloom",
    "Bees buzz",
    "Crickets chirp",
    "Stars shine",
    "Snow falls",
    "Sunsets glow",
    "Moon rises",
    "Dreams come",
]
def say(thing):
    engine.say(thing)
    engine.runAndWait()


engine.setProperty('volume',1.0)
def return_volume():
    volume = engine.getProperty('volume')
    return volume
def start(thing_to_say):
    say(thing_to_say)

def check(entry, text):
    print(return_volume())
    thing_to_say = text
    print(thing_to_say.lower())
    print(entry.get().lower())
    if entry.get().lower() == thing_to_say.lower():
        correct = messagebox.askyesno("Good","You have answered correctly. Continue?")
        if correct == 'yes':
            volumee = return_volume()
            engine.setProperty('volume',volumee-0.5)
            start(thing_to_say)
    else:
        if return_volume() < 0.5:
            messagebox.showinfo("Very bat njews","You shall see a doctor")
        print("bbb")


def layout_create():
    root = Tk()
    thingtosay = random.choice(vety)
    button = Button(command=lambda : start(thingtosay),text="start")
    button.grid(row=0)
    entry = Entry()
    entry.grid(row=1)
    checkbtn = Button(text="check", command = lambda : check(entry,thingtosay))
    checkbtn.grid(row=2)
    root.mainloop()









layout_create()

