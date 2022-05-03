from tkinter import *
from tkinter import ttk
import tkinter as tk

def entry(root):
    E1 = ttk.Entry(root)
    E1.pack(fill=tk.X, padx=5, pady=5)
    return E1