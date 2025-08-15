from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# --------------------all the app-functions--------------------#
try:
    data = pandas.read_csv(
        "C:/Users/akash/OneDrive/Documents/Python/Projects/flash-card-app/data/french_words_tolearn.csv"
    )
except FileNotFoundError:
    data = pandas.read_csv(
        "C:/Users/akash/OneDrive/Documents/Python/Projects/flash-card-app/data/french_words.csv"
    )

french_word = random.choice(data.French.to_list())
meaning = ((data[data.French == french_word]).English).item()
to_learn = data.to_dict(orient="records")


def flip_card(count):
    # HACK: Then this function will count till 5 sec and then will flip the card again and show the answer
    if count > 0:
        global flip_timer
        flip_timer = window.after(1000, flip_card, count - 1)
    else:
        canvas.itemconfig(first_image, image=flip_card_image)
        canvas.itemconfig(language_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=meaning, fill="white")


def right():
    # HACK: This function , after pressing the right button, remove that word from the list and make a new file without that word then
    # it randomly choose a diffrent word and its meaning then it will flip the card and show those french words and at last it will call
    # flip_card function
    global french_word, meaning

    for i in to_learn:
        if i["French"] == french_word:
            to_learn.remove(i)
            break

    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv(
        "C:/Users/akash/OneDrive/Documents/Python/Projects/flash-card-app/data/french_words_tolearn.csv",
        index=False,
    )

    window.after_cancel(flip_timer)
    french_word = random.choice(data.French.to_list())
    meaning = ((data[data.French == french_word]).English).item()

    canvas.itemconfig(first_image, image=card_photo)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    flip_card(5)


def wrong():
    window.after_cancel(flip_timer)
    global french_word, meaning
    french_word = random.choice(data.French.to_list())
    meaning = ((data[data.French == french_word]).English).item()

    canvas.itemconfig(first_image, image=card_photo)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    flip_card(5)


# ------------------- UI SETUP ---------------- #
# NOTE: creating the main window for the program to run
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# NOTE: creating cards
canvas = Canvas(width=800, height=526)
card_photo = PhotoImage(
    file="C:/Users/akash/OneDrive/Documents/Python/Projects/flash-card-app/images/card_front.png"
)
flip_card_image = PhotoImage(
    file="C:/Users/akash/OneDrive/Documents/Python/Projects/flash-card-app/images/card_back.png"
)
first_image = canvas.create_image(400, 263, image=card_photo)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# NOTE: creating the buttons
right_arrow_image = PhotoImage(
    file="C:/Users/akash/OneDrive/Documents/Python/Projects/flash-card-app/images/right.png"
)
wrong_arrow_image = PhotoImage(
    file="C:/Users/akash/OneDrive/Documents/Python/Projects/flash-card-app/images/wrong.png"
)

right_button = Button(image=right_arrow_image, highlightthickness=0, command=right)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_arrow_image, highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=0)

# NOTE: creating text on the cards
language_text = canvas.create_text(
    400, 163, text="French", font=("Ariel", 40, "italic")
)
flip_card(5)
word_text = canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))


window.mainloop()
