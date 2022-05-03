# Import docx NOT python-docx
import docx
from docx.shared import Pt

# Create an instance of a word document
doc = docx.Document()

# Add a Title to the document
doc.add_heading('Name of the department: ', 0)

# Adding paragraph with Increased font size
y = doc.add_heading('Increased Font Size Paragraph:', 3)

para = doc.add_paragraph().add_run(
	'GeeksforGeeks is a Computer Science portal for geeks.')
# Increasing size of the font
para.font.size = Pt(12)
para.font.underline = True
para.font.bold = True

# Adding paragraph with normal font size
doc.add_heading('Normal Font Size Paragraph:', 3)
doc.add_paragraph(
	'GeeksforGeeks is a Computer Science portal for geeks.')

y = doc.add_heading(f'Course Closing Report', 4)
y.add_run()
title_style = y.style
title_style.font.name = "Times New Roman"

# Now save the document to a location
doc.save('../Closing_report/gfg.docx')
