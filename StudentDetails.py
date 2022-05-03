# Import pandas
import pandas as pd
import tkinter as ttk
import tkinter as tk
from tkinter import *

# Load the xlsx file
excel_data = pd.read_excel('attainment.xlsx', header=None)
total_students = excel_data.shape[0]

def label_handler(text):
    label = ttk.Label(text=text)
    label.pack(fill=tk.X, padx=5, pady=5)

all_enrolls = excel_data[0].to_string(index=False).split('\n')
all_names = excel_data[1].to_string(index=False).split('\n')

root = Tk()
root.title('Marks')
root.geometry('1000x800')
for i in range(total_students):
    label_handler(f"{all_enrolls[i] + ' ' + all_names[i]}")

root.mainloop()
# all_enrolls = excel_data[0].to_string(index=False).split('\n')
# all_names = excel_data[1].to_string(index=False).split('\n')
# for i in range(total_students):
#     print(all_enrolls[i], all_names[i])
    # print(type(excel_data[0].to_string(index=False)))
