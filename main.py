from tkinter import * 
import math

BLACK = '#000000'
a = 1
FONT_NAME = "Courier"
types = {'*':"MULTIPLICATION",
         "+":"ADDITION", 
         "-":"SUBTRACTION",
         "/":"DIVISION"}


# ---------------------------- UI SETUP ------------------------------- #
window = Tk() 
window.title("Math Challenge")
window.config(padx=50, pady= 50, bg=BLACK, height= 500, width=500)

operator = Label(text=types["*"], font=(FONT_NAME, 45, "bold"), bg=BLACK)
operator.grid(column=2, row=0, pady=(0,5))

correct = Label(text=f"Correct: {a} | Missed {a}", font=(FONT_NAME, 45, "bold"), bg=BLACK)
correct.grid(column=2, row=1)

num_1 = Label(text=f"{a}", bg=BLACK, font=(FONT_NAME, 45, "bold"))
num_1.grid(column=2, row=2, pady=(10,0))

num_2 = Label(text=f"{a}", bg=BLACK, font=(FONT_NAME, 45, "bold"))
num_2.grid(column=2, row=3, pady=(0,0))

line = Label(text = "--------", bg=BLACK, font=(FONT_NAME, 45, "bold"))
line.grid(column=2, row=4, pady=(0,0))

# answer = Entry

window.mainloop()
