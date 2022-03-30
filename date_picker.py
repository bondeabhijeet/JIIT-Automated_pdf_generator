# Import Required Library
from tkinter import *
from tkcalendar import Calendar

def datepicker():
	# Create Object
	root = Tk()
	root.title('Select a date')
	root.iconbitmap('download.ico')
	# Set geometry
	root.geometry("270x350")

	# Add Calendar
	cal = Calendar(root, selectmode = 'day',
				year = 2020, month = 5,
				day = 22)

	cal.pack(pady = 20)

	def grad_date():
		print(cal.get_date())
		date.config(text = "Selected Date is: " + cal.get_date())

	# Add Button and Label
	Button(root, text = "Get Date",
		command = grad_date).pack(pady = 20)

	date = Label(root, text = "")
	date.pack(pady = 20)

	# Execute Tkinter
	root.mainloop()
