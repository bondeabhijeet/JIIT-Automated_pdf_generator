import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
import main2 as M2


def label_handler(text, rorw, cocl):
    label = ttk.Label(root1 ,text=text)
    label.grid(row=rorw, column=cocl)

def write_json(new_data, filename='details.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["COS"].append(new_data)           # Join new_data with file_data inside COS
        file.seek(0)                                # Sets file's current position at offset.
        json.dump(file_data, file, indent = 4)

def save_cos():
    entry_values = {}

    for i in range(len(my_entries)):
        entry = my_entries[i]
        entry_cog = cognitive_levels[i]
        entry_values[f'{i}'] = [entry.get(), entry_cog.get()]

    write_json(entry_values)
    root1.destroy()
    M2.in_it()


def COS(no_of_COS):
    global root1
    global my_entries
    global cognitive_levels
    
    root1 = tk.Tk()
    root1.geometry('1000x800')
    root1.title("Enter CO'S")
    # root1.columnconfigure(2, weight=3)
    
    my_entries = []
    cognitive_levels = []
    
    for i in range (no_of_COS):
        label_handler(f'CO{i+1}', i, 1)
        my_entry = ttk.Entry(root1)
        my_entry.grid(row=i, column=2, ipadx=70, ipady=7)
        my_entries.append(my_entry)

        label_handler(f'CO{i+1} cognitive level', i, 4)
        my_entry_cog = ttk.Entry(root1)
        my_entry_cog.grid(row=i, column=5, ipadx=70, ipady=7)
        cognitive_levels.append(my_entry_cog)

    save_butt = ttk.Button(root1, text="Save CO's and proceed", command=save_cos)
    save_butt.grid(row=i+1, column=4)

    root1.mainloop()
