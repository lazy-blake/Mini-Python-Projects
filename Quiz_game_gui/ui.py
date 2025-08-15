from tkinter import Button, Label, PhotoImage, Tk, Canvas
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz_game_gui")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

        wrong_image = PhotoImage(
            file="OneDrive/Documents/Python/Projects/Quiz_game_gui/images/false.png"
        )
        right_image = PhotoImage(
            file="OneDrive/Documents/Python/Projects/Quiz_game_gui/images/true.png"
        )
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="",
            font=("Arial", 20, "italic"),
            width=280,
        )

        # The right and wrong buttons
        self.wrong_button = Button(
            image=wrong_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.wrong_button_call,
        )
        self.right_button = Button(
            image=right_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.right_button_call,
        )

        self.wrong_button.grid(row=2, column=0, padx=20, pady=20)
        self.right_button.grid(row=2, column=1, padx=20, pady=20)

        # score
        self.score = Label(
            text="Score = 0",
            bg=THEME_COLOR,
            font=("Arial", 13, "bold"),
            fg="white",
        )
        self.score.config(padx=20, pady=20)
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.configure(bg="white")
            self.score.config(text=f"Score = {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.question_text, text="That's all for now")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_button_call(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def wrong_button_call(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.configure(bg="green")

        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)
