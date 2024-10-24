from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question",
            fill=THEME_COLOR,
            font=("Arial", 20,"italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0)
        self.true.grid(column=0, row=2)

        self.false = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0)
        self.false.grid(column=1, row=2)

        self.score = Label(text=f"score:0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)




        self.window.mainloop()