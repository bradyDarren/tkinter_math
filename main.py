from tkinter import * 
import math

BLACK = '#000000'
a = 1

# creation of the window.
window = Tk() 
window.title("Math Challenge")
window.config(padx=50, pady= 50, bg=BLACK, height= 500, width=500)

correct = Label(text=f"Correct: {a} | Missed {a}")
correct.grid(column=0, row=0)

window.mainloop()