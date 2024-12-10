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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
   count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)


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

reset_button=Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2,row=2)

check_marks=Label(text="✅",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)


window.mainloop()
