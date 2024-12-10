from subprocess import check_output
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    # Cancel any ongoing countdown
    if timer is not None:
        window.after_cancel(timer)
        timer = None  # Reset the timer variable

    # Reset the UI and other variables
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # Long break
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # Short break
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        # Work session
        count_down(work_sec)
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count>0:
     global timer
     timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✅"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Load the image
image = PhotoImage(file="tomato.png")

# Create a canvas with dimensions matching the image
canvas = Canvas(width=image.width(), height=image.height(), bg=YELLOW, highlightthickness=0)
canvas.create_image(image.width() // 2, image.height() // 2, image=image)

# Add timer text
timer_text = canvas.create_text(
    image.width() // 2,
    image.height() // 2 + 20,  # Adjust for positioning
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# Add a label above the canvas for "Timer"
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)


window.mainloop()
