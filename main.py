from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text= "Timer")
    check_mark.config(text= "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text= "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label.config(text="Work", fg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec< 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count> 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks+= "✔"
        check_mark.config(text= marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg= GREEN)
t_image = PhotoImage(file= "tomato.png")
canvas = Canvas(width = 200, height = 224, bg= GREEN, highlightthickness= 0)
canvas.create_image(100,112,image=t_image)
timer_text= canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row= 1)
label = Label(text= "Timer", fg= PINK, bg= GREEN, font=(FONT_NAME, 40))
label.grid(column=1, row= 0)
button_1= Button(text= "Start", highlightthickness=0, command= start_timer)
button_1.grid(column = 0, row= 2)
button_2= Button(text= "Reset", highlightthickness=0, command = reset_timer)
button_2.grid(column = 2, row= 2)
check_mark = Label(text ="✔", fg = PINK, bg = GREEN, font= 6)
check_mark.grid(column= 1, row= 3)


window.mainloop()