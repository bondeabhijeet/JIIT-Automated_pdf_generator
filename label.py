from tkinter import *
from tkinter import ttk


def label(root, labelOptions):
    global var
    var = StringVar()
    label = ttk.Label( root, textvariable=var, relief=RAISED)

    var.set(f"{labelOptions}")
    label.pack()