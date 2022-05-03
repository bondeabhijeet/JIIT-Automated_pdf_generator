from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkcalendar import Calendar
import entry as ET
import WriteExcel as WE

book, sheet = WE.xlwt_init()

root = tk.Tk()
root.geometry('500x600')
# root.iconbitmap('download.ico')
# root.resizable(False, False)
root.title('Attainment T1')

def grad_date():
	print(cal.get_date())    
	date.config(text = "Selected Date is: " + cal.get_date())

def datepicker():
    global cal
    global date
    root = Tk()
    root.title('Select a date')
    root.geometry('270x350')
    cal = Calendar(root, selectmode='day', year=2022, month=5, day=1)
    cal.pack(pady=20)
    Button(root, text='Get date', command=grad_date).pack(pady=20)

    date = Label(root, text="")
    date.pack(pady=20)

    root.mainloop()
 

def xls(Academic_Year, Course_name_code, Course_Cordinator, NBA_Code):

    WE.xlwt_merge_write(sheet, 0, 1, 0, 17, '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tJAYPEE INSTITUTE OF INFORMATION TECHNOLOGY')
    WE.xlwt_merge_write(sheet, 2, 2, 0, 1, f'Academic Year: {Academic_Year}')
    WE.xlwt_merge_write(sheet, 4, 5, 0, 7, f'Course name: {Course_name_code}')
    WE.xlwt_merge_write(sheet, 6, 7, 0, 3, f'Date of examination: {cal.get_date()}')
    WE.xlwt_merge_write(sheet, 6, 7, 5, 8, f'Course Cordinator: {Course_Cordinator}')
    WE.xlwt_merge_write(sheet, 6, 7, 9, 11, f'NBA Code: {NBA_Code}')
    WE.xlwt_save(book)

# Fetch Entry() values
def get_value():

    Academic_Year = Aca_year.get()
    NBA_Code = Nba_code.get()
    Course_name_code = Course_namecode.get()
    Course_Cordinator = Course_cordinator.get()

    print(Course_Cordinator)
    print(Course_name_code)
    print(Academic_Year)
    print(NBA_Code)
   
    xls(Academic_Year, Course_name_code, Course_Cordinator, NBA_Code)
    root.destroy()



def radio_get():

    radioValue = str(v.get())
    WE.xlwt_merge_write(sheet, 2, 2, 2, 3, f'Semester:{radioValue}')
    print(radioValue)
    
def radio(root, radioOptions):
    global v
    v = StringVar(root, "1")
    
    # Dictionary to create multiple buttons
    values = radioOptions

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values.items():
        Radiobutton(root, text = text, variable = v,
                    value = value, indicator = 0,
                    background = "light blue", command=radio_get).pack(fill = X, ipady = 5)


# Creating dropdown menu
def dropdown(labels, values_avaliable, exam):


    label = ttk.Label(text=labels[0])
    label.pack(fill=tk.X, padx=5, pady=5)

    # create a combobox
    selected_month = tk.StringVar()
    combo_box = ttk.Combobox(root, textvariable=selected_month, width=4)

    # get first 3 letters of every month name
    combo_box['values'] = values_avaliable

    # prevent typing a value
    combo_box['state'] = 'readonly'

    # place the widget
    combo_box.pack(fill=tk.X, padx=5, pady=5)


    # bind the selected value changes
    def month_changed(event):
        global exam
        print(selected_month.get())
        """ handle the month changed event """
        showinfo(
            title='Result',
            message=f'You selected {selected_month.get()}!'
        )
        exam = selected_month.get()
        WE.xlwt_merge_write(sheet, 2, 2, 4, 5, f'Examination:{exam}')


    combo_box.bind('<<ComboboxSelected>>', month_changed)


def label_handler(text):
    label = ttk.Label(text=text)
    label.pack(fill=tk.X, padx=5, pady=5)

label_handler("Enter academic year")
Aca_year = ET.entry(root)
radio(root, {"OddSem" : "Odd Semester", "EvenSem" : "Even Semester"})

labels = ['Examination']
values_avaliable = ['T1', 'T2', 'T3']
dropdown(labels, values_avaliable, '')

label_handler("Course name and code")
Course_namecode = ET.entry(root)

label_handler("Date of examination")
butt = ttk.Button(text='Select Date', command=datepicker)
butt.pack(fill=tk.X, padx=5, pady=5)

label_handler("Course Cordinator")
Course_cordinator = ET.entry(root)

label_handler("NBA CODE")
Nba_code = ttk.Entry(textvariable='NBA CODE')
Nba_code.pack(fill=tk.X, padx=5, pady=5)

butt1 = ttk.Button(text='SAVE CHANGES', command=get_value)
butt1.pack(fill=tk.X, padx=5, pady=5)

root.mainloop()