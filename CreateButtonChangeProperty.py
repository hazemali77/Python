#!/usr/bin/python3.6
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("1st GUI")
alabel=ttk.Label(win, text="Hello world")
alabel.grid(column=0, row=0)
# Button click event Function

def clickme():
	action.configure(text="** I have been clicked**")
	alabel.configure(foreground='red')
	alabel.configure(text="A Red Label")
# adding a Button
action=ttk.Button(win, text="Click me", command=clickme)
action.grid(column=1, row=0)

win.mainloop()
