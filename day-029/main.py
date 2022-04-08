from tkinter import Canvas, Tk, PhotoImage, Label, Entry, Button, END,\
                    messagebox

# ---------------------------- PASSWORD GENERATOR -------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = entry_website.get()
    username = entry_email_uname.get()
    password = entry_password.get()
    with open("./data.txt", mode="a") as data:
        data.write(f"{website} | {username} | {password}\n")
    entry_website.delete(0, END)
    entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0, "default@example.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
