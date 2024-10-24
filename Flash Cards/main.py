from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=back)


def is_known():
    to_learn.remove(current_card)
    datas = pandas.DataFrame(to_learn)
    datas.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="Title")
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="Word")

right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
