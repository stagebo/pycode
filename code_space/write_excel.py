
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

            len_dataij = 0
            for s in str(data[i][j]):
                if u'\u4e00' <= s <= u'\u9fff':  # 判断是否有中文
                    len_dataij += 2.9
                else:
                    len_dataij += 1.3
            col_widths[j] = max(col_widths[j], int(len_dataij))

            # col_widths[j] = max(col_widths[j],len(bytes(data[i][j],encoding='utf-8')),len(data[i][j]))
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


def create_excel(datas, file_name, sheets=[]):
    """
    写入数据到Excel，无合并单元格
    xlwt缺点：
        版本
        只能处理Excel97-2003或Excel 97之前版本的xls格式
        存储数据过大
        存储数据过大时，会报错Exception: String longer than 32767 characters
    :param data:
    :param merge_info:
    :param file_name:
    :param hdc:
    :param sheetname:
    :return:
    """
    wb = xlwt.Workbook(encoding='utf-8')
    # 设置单元格样式
    # height 300,
    style = xlwt.easyxf(
        '''
        font:
            height 280,
            name 宋体,
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
    # style.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    # style.pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    if len(datas) != len(sheets):
        sheets = ["sheet%s"%(i+1) for i in range( len(datas))]
    for sheetidx,data in enumerate(datas) :
        # 创建sheet
        sheetname = sheets[sheetidx]
        sheet = wb.add_sheet(sheetname, cell_overwrite_ok=True)

        # 记录列宽
        col_widths = [3 for i in range(0, max([len(j) for j in data]))]
        for i in range(len(data)):
            for j in range(len(data[0])):
                v = "" if (data[i][j] == None or str(data[i][j]).lower() == "none") else data[i][j]
                len_dataij = 0
                for s in str(data[i][j]):
                    if u'\u4e00' <= s <= u'\u9fff': # 判断是否有中文
                        len_dataij += 2.9
                    else:
                        len_dataij += 1.3
                col_widths[j] = max(col_widths[j], int(len_dataij))
                # print(data[i])
                # pattern = xlwt.Pattern()
                # pattern.pattern = xlwt.Pattern.SOLID_PATTERN
                # status = int(data[i][-1])
                # if  status == 403:
                #     pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']  # 设置单元格背景色为黄色
                # elif status == 401 or status == 200:
                #     pattern.pattern_fore_colour = xlwt.Style.colour_map['green']
                # elif status == 500:
                #     pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
                # else:
                #     pattern.pattern_fore_colour = xlwt.Style.colour_map['purple_ega']  # 设置单元格背景色为黄色
                # style.pattern = pattern
                maxlen = 32766
                v = v if (len(str(v)) < maxlen) else v[0:maxlen]

                sheet.write(i, j, v, style)

        # 设置列宽
        for i in range(len(col_widths)):
            wid = min(300 * (col_widths[i] + 1), 65535)
            sheet.col(i).width = wid


    wb.save(file_name)
    return True

if __name__ == "__main__":
    data = [['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','d','水电费'],
            ['啊','','发顺丰 房东的 得到的的']]
    filename = '../data/test.xls'
    _create_excel(data,filename)