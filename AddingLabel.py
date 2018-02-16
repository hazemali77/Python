#!/usr/bin/python3.6
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("1st GUI")
ttk.Label(win, text="Hello world").grid(column=0, row=0)
# win.resizable(0, 0.0)
win.mainloop()
