#!/usr/bin/env python3.6
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("LEARNING PYTHON GUI")
alabel=ttk.Label(win, text="A Label")
alabel.grid(column=0, row=0)
# Modified Button click  Function

def clickme():
	action.configure(text='Hellooo ' + name.get() + ' ' + numberChosen.get())
	
# adding a Button




ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a text box entry widget
name = tk.StringVar()
nameEntered=ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a button
action=ttk.Button(win, text="Click me", command=clickme)
action.grid(column=2, row=1)
### Disable the button
#action.configure(state='disabled')

ttk.Label(win, text="Choose a number").grid(column=1, row=0)
number=tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 3, 43, 600)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

#Creating three checkbuttons
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win, text="disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=1, row=4, sticky=tk.W)

# Bytton N. two

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win, text="unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=2, row=4, sticky=tk.W)

#Button No. three
chVarEn=tk.IntVar()
check3=tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=3, row=4, sticky=tk.W)

COLOR1="Blue"
COLOR2="Gold"
COLOR3="Red"

# Radio Button Callback


def radCall():
	radSel=radVar.get()
	if radSel == 1: win.configure(background=COLOR1)
	elif radSel == 2:win.configure(background=COLOR2)
	elif radSel == 3: win.configure(background=COLOR3)
# Create Radio buttons
radVar=tk.IntVar()
rad1=tk.Radiobutton(win, text=COLOR1, value=1, variable=radVar, command=radCall)
rad1.grid(column=1, row=5, sticky=tk.W)

rad2=tk.Radiobutton(win, text=COLOR2, value=2, variable=radVar, command=radCall)
rad2.grid(column=2, row=5, sticky=tk.W)

rad3=tk.Radiobutton(win, text=COLOR3, value=3, variable=radVar, command=radCall)
rad3.grid(column=3, row=5, sticky=tk.W)

# USing a scroll Text Control

scrollW = 30
scrollH = 3
scr = scrolledtext.ScrolledText(win, width=scrollW, height=scrollH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)


#Place cursor into name entry
nameEntered.focus()
win.mainloop()
