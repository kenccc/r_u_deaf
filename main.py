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
    engine.setProperty('volume',1.0)
    engine.say(thing)
    engine.runAndWait()


def return_volume():
    volume = engine.getProperty('volume')
    return volume
  
def start():
    said = random.choice(vety)
    say(said)
    return said

def check(entry, text):
    print(return_volume())
    thing_to_say = text
    print(thing_to_say.lower())
    print(entry.get().lower())
    if entry.get().lower() == thing_to_say.lower():
        correct = messagebox.askquestion("Good","You have answered correctly. Continue?")
        if correct == 'yes':
            volumee = return_volume()
            engine.setProperty('volume',volumee-0.5)
            quit()




    else:
        if return_volume() < 0.5:
            messagebox.showinfo("Very bat njews","You shall see a doctor")
        print("bbb")


def create_window(parent, sentence):
    new_window = Toplevel(parent)
    new_window.title(sentence)
  
    btn = Button(new_window)
    btn.grid(row=0)
    checkbtn = Button(new_window, text="check", command=lambda: check(entry, sentence))
    checkbtn.grid(row=2)
    sentence = start()
    entry = Entry(new_window)
    entry.grid(row=1)

    #button = Button(command=lambda: start(), text="start")
    #button.grid(row=0)

def main():
    root = Tk()
    create_button = Button(root, text="testme", command=lambda: create_window(root, start()))
    create_button.pack()
    root.mainloop()
  
main()



