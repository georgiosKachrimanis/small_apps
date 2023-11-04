from tkinter import *
import random 
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FILL_COLOR = "#0C356A"

try:
    df = pd.read_csv("wordcard/data/words_need_to_learn.csv")
    print("Using the new file!")
except FileNotFoundError:
    df = pd.read_csv("wordcard/data/Nederalnds_English_5k.csv")
    
word_dictionary = df.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer

    flip_timer = window.after_cancel(flip_timer)
    current_card = random.choice(word_dictionary)
        
    card.itemconfig(card_image, image=front_img)
    # We use the dictionary as a list just to make it more robust. From now on it will not matter which language you are using for your questions or your answers.
    card.itemconfig(card_title, text=list(current_card.keys())[0], fill=FILL_COLOR)
    card.itemconfig(card_word, text=list(current_card.values())[0], fill=FILL_COLOR)
    flip_timer = window.after(3000, func=answer_card)
        
def answer_card():   
    
    card.itemconfig(card_image, image=back_img)
    card.itemconfig(card_title, text=list(current_card.keys())[1], fill='white')
    card.itemconfig(card_word, text=list(current_card.values())[1], fill='white')
    

def is_known():
    word_dictionary.remove(current_card)
    df = pd.DataFrame(word_dictionary)
    df.to_csv("wordcard/data/words_need_to_learn.csv", index=False)
    next_card()
   


#===================UI==================================================

window = Tk()

window.title("Flash Cards!")
window.config( padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer =  window.after(3000, func=answer_card)

#Card image 
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="wordcard/images/card_front.png")
back_img =  PhotoImage(file="wordcard/images/card_back.png")
card_image = card.create_image(400, 263, image=front_img) # We will manipulate this image depending if we have the question or the answer.
# Image Text (Title)
card_title = card.create_text(400, 150, text="", fill=FILL_COLOR, font=("Ariel", 40, "italic")) 
# Image Text (Word)
card_word = card.create_text(400, 263, text="", fill=FILL_COLOR, font=("Ariel", 60, "bold")) 

card.grid(row=0, column=0, columnspan=2)

# Buttons
not_known_word_img = PhotoImage(file="wordcard/images/wrong.png")
not_known_word = Button(image=not_known_word_img, highlightthickness=0, borderwidth=0, command=next_card)
not_known_word.grid(row=1, column=0, padx=10, pady=10)

known_word_img = PhotoImage(file="wordcard/images/right.png")
known_word = Button(image=known_word_img, highlightthickness=0, borderwidth=0, command=is_known )
known_word.grid(row=1, column=1,  padx=10, pady=10)

next_card()



window.mainloop()