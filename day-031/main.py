from tkinter import Tk, Canvas, PhotoImage, Button, Label

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 200, image=card_front)
canvas.grid(column=1, row=1, columnspan=2, rowspan=3)

title = Label(text="Title", bg="white", fg="black")
title.grid(column=1, row=1, columnspan=2)

word = Label(text="Word", bg="white", fg="black")
word.grid(column=1, row=2, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0)
cross_button.grid(column=1, row=4)

tick_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0)
tick_button.grid(column=2, row=4)

window.mainloop()
