from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()

        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50)
        self.label = Label(text="SCORE 0", fg="white", bg=THEME_COLOR, font=("arial", 10, "bold"))
        self.label.grid(column=2, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text((150, 125),
                                                     width=280,
                                                     text="QUESTIONS COMING",
                                                     fill=THEME_COLOR,
                                                     font=("arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=3, pady=20)

        self.right = PhotoImage(file="images/true.png")
        self.wrong = PhotoImage(file="images/false.png")
        self.tick_button = Button(image=self.right, highlightthickness=0, command=self.true)
        self.tick_button.grid(row=2, column=0)
        self.tick_button.config(padx=20, pady=20)

        self.cross_button = Button(image=self.wrong, highlightthickness=0, command=self.false)
        self.cross_button.config(padx=20, pady=20)
        self.cross_button.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Thanks for playing.\n Your final score is {self.quiz.score}/10")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true(self):
        self.quiz.check_answer("true")

        if self.quiz.current_question.answer.lower() == "true":
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def false(self):
        self.quiz.check_answer("false")

        if self.quiz.current_question.answer.lower() == "false":
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

