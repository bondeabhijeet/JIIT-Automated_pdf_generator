import tkinter as tk
from tkinter import *
from tkinter import ttk
import json

def label_handler(text):
    label = ttk.Label(root1 ,text=text)
    label.pack(fill=tk.X, padx=5, pady=5)

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

def COS(no_of_COS):
    global root1
    global my_entries
    global cognitive_levels

    root1 = tk.Tk()

    my_entries = []
    cognitive_levels = []
    
    for i in range (no_of_COS):
        label_handler(f'CO{i}')
        my_entry = ttk.Entry(root1)
        my_entry.pack(fill=tk.X, padx=25, pady=5)
        my_entries.append(my_entry)

        label_handler(f'CO{i} cognitive level')
        my_entry_cog = ttk.Entry(root1)
        my_entry_cog.pack(fill=tk.X, padx=25, pady=5)
        cognitive_levels.append(my_entry_cog)

    save_butt = ttk.Button(root1, text="Save CO's", command=save_cos)
    save_butt.pack(fill = tk.X, padx=5, pady=5)

    root1.mainloop()
