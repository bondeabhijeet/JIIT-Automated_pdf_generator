# # Writing to an excel
# # sheet using Python
# import xlwt
# from xlwt import Workbook

# # Workbook is created
# wb = Workbook()

# # add_sheet is used to create sheet.
# sheet1 = wb.add_sheet('Sheet 1')

# sheet1.write(1, 0, 'ISBT DEHRADUN')
# sheet1.write(2, 0, 'SHASTRADHARA')
# sheet1.write(3, 0, 'CLEMEN TOWN')
# sheet1.write(4, 0, 'RAJPUR ROAD')
# sheet1.write(5, 0, 'CLOCK TOWER')
# sheet1.write(0, 1, 'ISBT DEHRADUN')
# sheet1.write(0, 2, 'SHASTRADHARA')
# sheet1.write(0, 3, 'CLEMEN TOWN')
# sheet1.write(0, 4, 'RAJPUR ROAD')
# sheet1.write(0, 5, 'CLOCK TOWER')

# wb.save('xlwt example.xls')
import xlwt

def xlwt_init():
    book = xlwt.Workbook()
    sheet = book.add_sheet('Test')
    return book, sheet

def xlwt_merge_write(sheet, r1, r2, c1, c2, MergeOptions, style):
    al = xlwt.Alignment()
    al.horz = xlwt.Alignment.HORZ_CENTER
    # B1: with style, there is wrap
    
    if style == '':
        style = xlwt.XFStyle()
        font = xlwt.Font()
        style.font = font
        style.font.height = 210
        # style = xlwt.XFStyle()
        # style.alignment.wrap = 1
        sheet.write_merge(r1, r2, c1, c2, MergeOptions, style=style)
    else:
        sheet.write_merge(r1, r2, c1, c2, MergeOptions, style=style)

# sheet.write(0, 1, 'Hello\nWorld', style)

def xlwt_save(book):
    book.save('7. Attainment T2.xls')
