from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}
# ---------------------import csv -------------------------
try:
    words = pandas.read_csv("data/words_2_Learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Spanish_English.csv")
    to_learn = original_data.to_dict(orient="records")
    print(to_learn)
else:
    to_learn = words.to_dict(orient="records")


# ---------------------Next_card-------------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(c_title, text="Spanish", fill="black")
    canvas.itemconfig(c_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(c_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------flip_card-------------------------------
def flip_card():
    canvas.itemconfig(c_title, text="English", fill="white")
    canvas.itemconfig(c_word, text=current_card["English"], fill="white")
    canvas.itemconfig(c_background, image=back_img)


# ---------------------is_known-------------------------------
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_2_Learn.csv", index=False)
    next_card()
# ---------------------UI-------------------------------

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
c_background = canvas.create_image(400, 263, image=front_img)
c_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
c_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, highlightthickness=0, command=is_known)
right.grid(column=1, row=1)

next_card()

window.mainloop()
