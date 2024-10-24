from tkinter import *

window = Tk()
window.title("Miles-Kilometer")
window.minsize(width=250,height=150)
window.config(padx=50,pady=50)

entry = Entry()
entry.grid(column=1,row=0)
entry.config(width=8)

miles = Label(text="Miles")
miles.grid(column=2,row=0)
miles.config(padx=10)

equal = Label(text="is equal to")
equal.grid(column=0,row=1)

def calculate():
    m = int(entry.get())
    kilometer.config(text=round(m*1.6,2))

kilometer = Label(text="0")
kilometer.grid(column=1,row=1)

calc = Button(text="Calculate",command=calculate)
calc.grid(column=1,row=2)

km = Label(text="Kilometer",padx=10)
km.grid(column=2,row=1)

window.mainloop()