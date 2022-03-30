from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
# import combo_box as CB
import os

root = Tk()
root.title("JIIT MENU")
root.iconbitmap('Y:\MinorProject\download.ico')
root.geometry('900x600')
root.configure(bg='#000000')
def Selected_File():
    selected_file = filedialog.askopenfilename(initialdir='C://', title='Select a file', filetypes = (("Text files", "*.docx*"),))
    print(selected_file)

def combo_execute():
    root.destroy()
    import combo_box

script_dir = os.path.dirname(__file__)
rel_path = ".\\JIIT.png"
abs_file_path = os.path.join(script_dir, rel_path)
image = Image.open(abs_file_path)
photo = ImageTk.PhotoImage(image)

label = Label(root, image = photo, border='0')
label.image = photo
label.grid(row=1)

but10=  ttk.Button(root, text='Subject Closing Report', command=Selected_File, width='20')
but10.grid(row='2',column='1', ipadx='10', ipady='10')

but11= ttk.Button(root, text='Overall Attainment', command=Selected_File, width='20')
but11.grid(row='2',column='2', ipadx='10', ipady='10')

but12= ttk.Button(root, text='Exit Survey', command=Selected_File, width='20')
but12.grid(row='2',column='3', ipadx='10', ipady='10')

but13= ttk.Button(root, text='Attainment T2', command=Selected_File, width='20')
but13.grid(row='2',column='4', ipadx='10', ipady='10')

but20= ttk.Button(root, text='Attainment Assignment', command=Selected_File, width='20')
but20.grid(row='3',column='1', ipadx='10', ipady='10')

but21= ttk.Button(root, text='Make_up Question Paper', command=Selected_File, width='20')
but21.grid(row='3',column='2', ipadx='10', ipady='10')

but22= ttk.Button(root, text='T2 Question Paper', command=Selected_File, width='20')
but22.grid(row='3',column='3', ipadx='10', ipady='10')

but23= ttk.Button(root, text='Attainment T1', command=combo_execute, width='20')
but23.grid(row='3',column='4', ipadx='10', ipady='10')

but30= ttk.Button(root, text='T1 Question Paper', command=Selected_File, width='20')
but30.grid(row='4',column='1', ipadx='10', ipady='10')

but31= ttk.Button(root, text='Assisgnment Solution', command=Selected_File, width='20')
but31.grid(row='4',column='2', ipadx='10', ipady='10')

but32= ttk.Button(root, text='Assignments', command=Selected_File, width='20')
but32.grid(row='4',column='3', ipadx='10', ipady='10')

but33= ttk.Button(root, text='Assessment Tool', command=Selected_File, width='20')
but33.grid(row='4',column='4', ipadx='10', ipady='10')

but40= ttk.Button(root, text='Lesson Plan', command=Selected_File, width='20')
but40.grid(row='5',column='1', ipadx='10', ipady='10')

but41= ttk.Button(root, text='Opening Report', command=Selected_File, width='20')
but41.grid(row='5',column='2', ipadx='10', ipady='10')

but42= ttk.Button(root, text='Closing Report', command=Selected_File, width='20')
but42.grid(row='5',column='3', ipadx='10', ipady='10')

but43= ttk.Button(root, text='Detailed Syllabus', command=Selected_File, width='20')
but43.grid(row='5',column='4', ipadx='10', ipady='10')

but10= ttk.Button(root, text='Detailed Syllabus', command=Selected_File, width='20')
but10.grid(row='6',column='1', ipadx='10', ipady='10')

but101= ttk.Button(root, text='PEOs & POs', command=Selected_File, width='20')
but101.grid(row='6',column='2', ipadx='10', ipady='10')

but102= ttk.Button(root, text='Mission Vission CSE&IT', command=Selected_File, width='20')
but102.grid(row='6',column='3', ipadx='10', ipady='10')

but103= ttk.Button(root, text='Mission Vission JIIT', command=Selected_File, width='20')
but103.grid(row='6',column='4', ipadx='10', ipady='10')



root.mainloop()
