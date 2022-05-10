import json
import WriteExcel as WE
import xlwt
import os

def attain_ment():
    with open('details.json', 'r+') as f:
        json_data = json.load(f)
    
    Academic_Year =  json_data['Acad_yar']
    Course_name = json_data['Course_name']
    Course_Code = json_data['Course_details']['Course_CODE']
    Course_Cordinator = json_data['Course_details']['Course_Cordinator']
    NBA_Code = json_data['Course_details']['NBA_CODE']
    T2_Date = json_data['T2_date']
    Semester = json_data['Sem']
    Branch = json_data['Prog_name']
    Examination = 'T2'

    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    style.font = font
    style.font.height = 302
    borders = xlwt.Borders()
    borders.bottom = xlwt.Borders.THICK
    style.borders = borders
   
    book, sheet = WE.xlwt_init()
    WE.xlwt_merge_write(sheet, 0, 1, 0, 17, '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tJAYPEE INSTITUTE OF INFORMATION TECHNOLOGY', style)
    WE.xlwt_merge_write(sheet, 2, 2, 0, 3, f'Academic Year: {Academic_Year}', '')
    WE.xlwt_merge_write(sheet, 4, 5, 0, 10, f'Course name: {Course_name} ({Course_Code})', '')
    WE.xlwt_merge_write(sheet, 6, 7, 0, 3, f'Date of examination: {T2_Date}', '')
    WE.xlwt_merge_write(sheet, 6, 7, 5, 8, f'Course Cordinator: {Course_Cordinator}', '')
    WE.xlwt_merge_write(sheet, 3, 3, 0, 3, f'NBA Code: {NBA_Code}', '')
    WE.xlwt_merge_write(sheet, 8, 9, 0, 2, f'Semester: {Semester}', '')
    WE.xlwt_merge_write(sheet, 8, 9, 5, 7, f'Branch: {Branch}', '')
    WE.xlwt_merge_write(sheet, 3, 3, 5, 7, f'Examination: {Examination}', '')
    
    WE.xlwt_merge_write(sheet, 4, 5, 12, 12, 'NOTE:', style)
    style1 = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    style1.font = font
    style1.font.height = 200
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THICK
    borders.bottom = xlwt.Borders.THICK
    style1.borders = borders

    style2 = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    style2.font = font
    style2.font.height = 200
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THICK
    borders.top = xlwt.Borders.THICK
    borders.right = xlwt.Borders.THICK
    borders.bottom = xlwt.Borders.THICK
    style2.borders = borders

    style3 = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = False
    style3.font = font
    style3.font.height = 200
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THICK
    borders.right = xlwt.Borders.THICK
    style3.borders = borders

    WE.xlwt_merge_write(sheet, 6, 6, 12, 15, f'% of Students Scored >= Target %', style2)
    WE.xlwt_merge_write(sheet, 7, 7, 12, 15, f'                               >= 80%', style3)
    WE.xlwt_merge_write(sheet, 8, 8, 12, 15, f'                               >= 70%', style3)
    WE.xlwt_merge_write(sheet, 9, 9, 12, 15, f'                                  60%', style3)
    WE.xlwt_merge_write(sheet, 10, 10, 12, 15, f'                               >=60%', style3)

    WE.xlwt_merge_write(sheet, 6, 6, 16, 17, f'Attainment Level', style2)
    WE.xlwt_merge_write(sheet, 7, 7, 16, 17, f'                  3', style3)
    WE.xlwt_merge_write(sheet, 8, 8, 16, 17, f'                  2', style3)
    WE.xlwt_merge_write(sheet, 9, 9, 16, 17, f'                  1', style3)
    WE.xlwt_merge_write(sheet, 10, 10, 16, 17, f'                  0', style3)




    style = xlwt.easyxf()
    style.font.colour_index = xlwt.Style.colour_map['red']
    style.font.height = 302
    sheet.write_merge(4, 5, 13, 14, f"Target % is 50 %", style=style)
    # sheet.write(10, 11, 'Some text', style)

    # WE.xlwt_merge_write(sheet, 19, 20, 0, 1, 'NOTE:', style)


    # style = xlwt.XFStyle()
    # # font
    # font = xlwt.Font()
    # font.bold = True
    # style.font = font
    # # borders
    # borders = xlwt.Borders()
    # borders.bottom = xlwt.Borders.DASHED
    # style.borders = borders
    # sheet.write_merge(20, 20, 19, 20, 'niceoo', style=style)
    # sheet.write(20, 20, 'test value', style=style)
    
    WE.xlwt_save(book)


    print(Academic_Year, Course_Cordinator, Course_Code, Course_name, NBA_Code)


    
attain_ment()
os.system("libreoffice '7. Attainment T2.xls'")

