import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "🍅"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks_label.config(text="")
    global reps
    reps = 0
    start_button.config(state="normal")
    reset_button.config(state="disabled")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global reps
    if reps == 8:
        reps = 0
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # # If it's the 1st / 3rd / 5th / 7th rep:
    # count_down(work_sec)
    # # If it's the 8th rep:
    # count_down(long_break_sec)
    # # If it's the 2nd / 4th / 6th:
    # count_down(short_break_sec)

    if reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Python is dynamically typed so we can change int to string
    if count_min < 10:
        count_min = "0" + str(count_min)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    time_left = f"{count_min}:{count_sec}"
    global timer
    canvas.itemconfig(timer_text, text=time_left)
    if count > 0:
        # Takes amount of time to wait and after that time it calls a particular function
        # Time is in ms
        # Extra *args is what we are going to pass into the function
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        canvas.itemconfig(timer_text, text="--:--")
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_marks += CHECK_MARK
        check_marks_label.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")  # Pomodoro means tomato in italian
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "normal"))
timer_label.grid(column=1, row=0)

# Canvas works in layers units are in pixels
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")  # Reads through file and gets hold of image
canvas.create_image(100, 112, image=tomato_img)  # Creates image in center
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)

# Check Mark Label
check_marks_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "normal"), padx=2, pady=2)
check_marks_label.grid(column=1, row=3)

window.mainloop()
