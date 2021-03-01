from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)
canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Trouve", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)



window.mainloop()