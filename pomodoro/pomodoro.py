from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = chr(0x2705)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
window = Tk()

def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    reps  = 0
    title_label.config(text="Timer", fg=GREEN)
    check_mark_area.config(text="")


def start_timer():
    global reps
    reps += 1

    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break!", fg=RED)
        check_mark_area.config(text=CHECK_MARK * 4)
        reps = 0  
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Sort Break!", fg=PINK)
        check_mark_area.config(text=CHECK_MARK * int(reps / 2))
    else:
        title_label.config(text="Working Session!", fg=GREEN)
        count_down(WORK_MIN * 60)


def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()


window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
title_label.grid(row=0, column=1)

# Tomato image.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img= PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start = Button(text="Start", borderwidth=1, highlightthickness=0, font=(FONT_NAME, 18, "bold"), command=start_timer)
start.grid(row=2, column=0)

start = Button(text="Reset", borderwidth=1, highlightthickness=0, font=(FONT_NAME, 18, "bold"), command=reset_timer)
start.grid(row=2, column=2)

# completed task check marks
check_mark_area = Label(bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_mark_area.grid(row=2, column=1)


window.mainloop()