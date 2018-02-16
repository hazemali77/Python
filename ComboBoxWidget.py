#!/usr/bin/python3.6
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("LEARNING PYTHON GUI")
alabel=ttk.Label(win, text="A Label")
alabel.grid(column=0, row=0)
# Modified Button click  Function

def clickme():
	action.configure(text='Hellooo' + name.get())
	
# adding a Button




ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a text box entry widget
name = tk.StringVar()
nameEntered=ttk.Entry(win, width=120, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a button
action=ttk.Button(win, text="Click me", command=clickme)
action.grid(column=2, row=1)
### Disable the button
#action.configure(state='disabled')

ttk.Label(win, text="Choose a number").grid(column=1, row=0)
number=tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 3, 43, 600)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)
#Place cursor into name entry
nameEntered.focus()
win.mainloop()
