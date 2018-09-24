
'''
__target__ =  写Excel文件
'''
import xlwt
def _create_excel(data  ,file_name ,merge_info=[] ,sheetname="sheet1"):
    print(merge_info)
    # wb = xlwt.Workbook(encoding='utf-8')
    wb = xlwt.Workbook()


    # 设置单元格样式
    style = xlwt.easyxf(
        '''
        font: 
            height 300,
            name 黑体, 
            colour_index black, 
            bold off, 
            italic off; 
        align: 
            wrap off, 
            vert centre, 
            horiz centre;
        borders:
            left 1,
            right 1,
            top 1,
            bottom 1;
        alignment:
            horz center,
            vert center;
        ''')


    sheet = wb.add_sheet(sheetname ,cell_overwrite_ok=True)

    # 记录列宽
    col_widths = [3 for i in range(0,max([len(j) for j in data]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            col_widths[j] = max(col_widths[j],len(bytes(data[i][j],encoding='utf-8')),len(data[i][j]))
            sheet.write(i ,j ,data[i][j] ,style)
    print(col_widths)
    # 设置列宽
    for i in range(len(col_widths)):
        sheet.col(i).width = 512 * ( col_widths[i] + 1)
    # print(col_widths)
    for mg in merge_info:
        a ,b ,c ,d = mg
        sheet.write_merge(a , b -1 ,c , d -1 ,data[a][c] ,style)
    # sheet.write_merge(0,3,0,2,'天涯共此时', style)

    wb.save(file_name)
    return True

if __name__ == "__main__":
    data = [['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','d','水电费'],
            ['啊','','发顺丰 房东的 得到的的']]
    filename = '../data/test.xls'
    _create_excel(data,filename)