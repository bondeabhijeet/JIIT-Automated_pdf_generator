from docx import Document
from docxcompose.composer import Composer
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.title('Merge mission vision and JIIT vision')
root.geometry('300x400')

files = []

def Selected_File():
    selected_file = filedialog.askopenfilename(initialdir='C://', title='Select a file', filetypes = (("Text files", "*.docx*"),))
    print(selected_file)
    files.append(selected_file)
    
    composed = "/home/kali/Downloads/composed.docx"

    print(files)
    result = Document(files[0])
    result.add_page_break()
    composer = Composer(result)

    for i in range(1, len(files)):
        doc = Document(files[i])

        if i != len(files) - 1:
            doc.add_page_break()

        composer.append(doc)

    composer.save(composed)

    if len(files) == 2:
        root.destroy()

but10=  ttk.Button(root, text='Select file Mission vision JIIT', command=Selected_File, width='20')
but10.pack(fill=tk.X, padx=5, pady=5)
but11=  ttk.Button(root, text='Select file Mission Vision (Department wise)', command=Selected_File, width='20')
but11.pack(fill=tk.X, padx=5, pady=5)

root.mainloop()