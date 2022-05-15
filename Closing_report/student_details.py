import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json

def read_details():
    df = pd.read_excel (selected_file)
    df.to_json('student_details.json')

def Selected_File_dia():
    global selected_file
    selected_file = filedialog.askopenfilename(initialdir='C://', title='Select a file', filetypes = (("Text files", "*.xlsx*"),))

def get_value_q():
    global No_of_ques
    No_of_ques = entr.get()
    root1.destroy()

root1 = tk.Tk()
root1.title("No of questions")
root1.geometry("400x400")
lab = ttk.Label(root1, text="Enter the number of questions (integer)")
lab.pack(fill=tk.X, padx=5, pady=5)

entr = ttk.Entry(root1)
entr.pack(fill=tk.X, padx=5, pady=5)

butt0 = ttk.Button(root1, text="Select student list file (.xlsx)", command=Selected_File_dia)
butt0.pack(fill=tk.X, padx=5, pady=5)

butt = ttk.Button(root1, text="Save number of questions", command=get_value_q)
butt.pack(fill=tk.X, padx=5, pady=5)

root1.mainloop()

with open('details.json', 'r+') as f:
        json_data = json.load(f)

No_Of_COS = len(json_data["COS"][0])
root = tk.Tk()

root.geometry('800x1000')
# root.resizable(False, False)
root.title('Combobox Widget')


COs_Question_map = []
Marks = []
butts = []
entrs = []

def json_update():
    json_data["CO_quest_map"] = COs_Question_map
    with open("details.json", 'w') as f:
        json.dump(json_data, f)

def get_value():
    for i in range(int(No_of_ques)):
        COs_Question_map.append((butts[i].get(), entrs[i].get()))
    json_update()
    root.destroy()

def butt_maker(qno):
    global selected_month
    
    label = ttk.Label(text=f"Please select CO for Q.no {qno+1}")
    label.pack(fill=tk.X, padx=5, pady=5)
    selected_month = tk.StringVar()
    month_cb = ttk.Combobox(root, textvariable=selected_month)
    month_cb['values'] = [f"CO {m}" for m in range(1, No_Of_COS+1)]
    month_cb['state'] = 'readonly'
    month_cb.pack(fill=tk.X, padx=5, pady=5)
    butts.append(month_cb)

    labe = ttk.Label(text=f"Total marks for Q.no {qno+1}")
    labe.pack(fill=tk.X, padx=5, pady=5)

    entr = ttk.Entry(root)
    entr.pack(fill=tk.X, padx=5, pady=5)
    entrs.append(entr)

for i in range(int(No_of_ques)):
    butt_maker(i)

butt = ttk.Button(root, text="Submit", command=get_value)
butt.pack(fill=tk.X, padx=5, pady=5)

root.mainloop()

read_details()