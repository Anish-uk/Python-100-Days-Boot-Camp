from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    try:
        with open("password.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops",message="No Data File Found")
    else:
        if website_entry.get() in data:
            messagebox.showinfo(title=website_entry.get(),message=f"Email:{data[website_entry.get()]['email']}\nPassword:{data[website_entry.get()]['password']}")
        else:
            messagebox.showinfo(title=website_entry.get(),message="No details for the website!")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_numbers+password_letters+password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }

    if len(email_user_entry.get())==0 or len(password_entry.get())==0 or len(website_entry.get())==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("password.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("password.json","w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,"end")
            email_user_entry.delete(0,"end")
            password_entry.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2,sticky="EW")
website_entry.focus()

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0,row=2)

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1,row=2,columnspan=2,sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=17)
password_entry.grid(column=1,row=3,sticky="EW")

generate_password = Button(text="Generate Password",command=generate_passwords)
generate_password.grid(column=2,row=3,sticky="EW")

add = Button(text="Add",width=36,command=save)
add.grid(column=1,row=4,columnspan=2,sticky="EW")

search = Button(text="Search",command=find_password)
search.grid(column=2,row=1,sticky="EW")











window.mainloop()