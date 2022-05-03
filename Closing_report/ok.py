# import xlwt


# book = xlwt.Workbook()

# # add new colour to palette and set RGB colour value
# xlwt.add_palette_colour("custom_colour", 0x21)
# book.set_colour_RGB(0x21, 251, 228, 228)
# style_pass = xlwt.easyxf('pattern: pattern solid, fore_colour white;')
# # now you can use the colour in styles
# sheet1 = book.add_sheet('Sheet 1')
# # style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
# style = xlwt.easyxf()
# style.font.colour_index = xlwt.Style.colour_map['red']
# sheet1.write(0, 0, 'Some text', style)

# book.save('test.xls')

import pandas as pd
import xlsxwriter


data = pd.DataFrame({f'% of Students Scored >= Target %':[1,2,3,4,5],
                   ' ':[2,3,4,5,6],
                   'Attainment Level':[3,4,5,6,7],
                   'd':[4,5,6,7,8],
                   'e':[5,6,7,8,9]})

workbook = xlsxwriter.Workbook("test1.xlsx")
worksheet = workbook.add_worksheet("sheli22")

header_format = workbook.add_format({
    'bold': True,
    'font_name': 'Arial',
    'font_size': 10,
    'text_wrap': True,
    'center_across': True,
    'valign': 'bottom',
    'fg_color': '#cdffff',
    'border': 1})
worksheet.set_column(0, 0, 35)
worksheet.set_column(0, 3, 35)


for col_num, value in enumerate(data.columns.values):
    worksheet.write(0, col_num, value, header_format)

worksheet.add_table('B3:F7', {'data': data.values.T.tolist(),'style': 'Table Style Light 22','autofilter': False})
# worksheet.add_table('B3:F7', {'data': data.values.T.tolist(),'style': 'Table Style Light 17','header_row': True})

workbook.close()