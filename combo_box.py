from struct import pack
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import date_picker as DP

root = tk.Tk()


root.geometry('500x600')
root.iconbitmap('download.ico')
# root.resizable(False, False)
root.title('Attainment T1')

def get_value():
    print(ent.get())

def dropdown(labels, values_avaliable):

    label = ttk.Label(text=labels[0])
    label.pack(fill=tk.X, padx=5, pady=5)

    # create a combobox
    selected_month = tk.StringVar()
    combo_box = ttk.Combobox(root, textvariable=selected_month, width=4)

    # get first 3 letters of every month name
    # combo_box['values'] = [month_name[m][0:3] for m in range(1, 13)]
    # combo_box['values'] = ['nice', 'ok']
    combo_box['values'] = values_avaliable

    # prevent typing a value
    combo_box['state'] = 'readonly'

    # place the widget
    combo_box.pack(fill=tk.X, padx=5, pady=5)


    # bind the selected value changes
    def month_changed(event):
        print(selected_month.get())
        """ handle the month changed event """
        showinfo(
            title='Result',
            message=f'You selected {selected_month.get()}!'
        )

    combo_box.bind('<<ComboboxSelected>>', month_changed)

def label_handler(text):
    label = ttk.Label(text=text)
    label.pack(fill=tk.X, padx=5, pady=5)

labels = ['Academic Year']
values_avaliable = ['2019-20', '2020-21', '2021-22']
dropdown(labels, values_avaliable)

labels = ['Examination']
values_avaliable = ['T1', 'T2', 'T3']
dropdown(labels, values_avaliable)

labels = ['Course name and code']
values_avaliable = ['Information Retieval and Semantic Web (16B1NCI648)']
dropdown(labels, values_avaliable)

label_handler("Date of examination")
butt = ttk.Button(text='Select Date', command=DP.datepicker)
butt.pack(fill=tk.X, padx=5, pady=5)

labels = ['Course Cordinator']
values_avaliable = ['Dr. Ankit Vidyarthi', 'Dr. Parul Agarwal', 'Dr. Pawan Kumar Upadhyay']
dropdown(labels, values_avaliable)

label_handler("NBA CODE")
ent = ttk.Entry(textvariable='NBA CODE')
ent.pack(fill=tk.X, padx=5, pady=5)

butt1 = ttk.Button(text='SAVE CHANGES', command=get_value)
butt1.pack(fill=tk.X, padx=5, pady=5)
root.mainloop()