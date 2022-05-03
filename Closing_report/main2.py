import tkinter as tk
from tkinter import *
from tkinter import ttk
import json

def write_json(new_data, filename='details.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
    
    file_data["Course_details"] =  new_data          # Join new_data with file_data inside COS
    
    with open(filename, 'w') as f:
        json.dump(file_data, f)

def get_value():
    Course_Code = Course_code.get()
    Course_Cordinator = Course_cor.get()
    Nba_Code = Nba_code.get()

    new_data = {'Course_CODE': f'{Course_Code}', 'Course_Cordinator': f'{Course_Cordinator}', 'NBA_CODE': f'{Nba_Code}'}
    write_json(new_data)
    
    root2.destroy()


def in_it():
    global root2
    root2 = tk.Tk()
    root2.geometry('1000x800')
    root2.title('More details')

    global Course_code
    global Course_cor
    global Nba_code

    ttk.Label(root2, text='Course Code').pack(fill=tk.X ,padx=5, pady=5)
    Course_code = ttk.Entry(root2)
    Course_code.pack(fill=tk.X, padx=5, pady=5)

    ttk.Label(root2, text='Course Cordinator').pack(fill=tk.X ,padx=5, pady=5)
    Course_cor = ttk.Entry(root2)
    Course_cor.pack(fill=tk.X, padx=5, pady=5)

    ttk.Label(root2, text='NBA CODE').pack(fill=tk.X ,padx=5, pady=5)
    Nba_code = ttk.Entry(root2)
    Nba_code.pack(fill=tk.X, padx=5, pady=5)

    butt1 = ttk.Button(text="SAVE CHANGES", command=get_value)
    butt1.pack(fill=tk.X, padx=5, pady=5)
    root2.mainloop()
# in_it()
