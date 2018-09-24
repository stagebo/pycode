
'''
__target__ = 读取excel内容，遇到合并单元格则拆分合并单元格
'''
import xlrd
import logging
def read_excel_as_merge(file_name):
    data = []
    wb = xlrd.open_workbook(file_name)

    sheet = wb.sheet_by_name(wb.sheet_names()[0])
    merge = sheet.merged_cells
    print('merge_info:',merge)
    for ri in range(sheet.nrows):
        # print(sheet.row_values(r))
        row = []
        for ci in range(sheet.ncols):
            v = sheet.cell(ri,ci).value
            if v == "":
                for rg in merge:
                    a,b,c,d = rg
                    if ri>=a and ri<b and ci>=c and ci<d:
                        v = sheet.cell(a,c).value
            row.append(v)
        data.append(row)

    return data

class Log():
    def write(self,s):
        print(s)

def merge_cell(sheet):
    rt = {}
    print('merge_info:', sheet.merged_cells)
    if sheet.merged_cells:
        # exists merged cell
        for item in sheet.merged_cells:
            for row in range(item[0], item[1]):
                for col in range(item[2], item[3]):
                    rt.update({(row, col): (item[0], item[2])})
    return rt

def get_merged(filename):
    # 这里本应该做filepath的判断，但是我先省略了
    book = xlrd.open_workbook(filename,logfile=Log(),formatting_info=True)
    sheets = book.sheets()    # 所有sheets
    for index in range(len(sheets)):
        sheet = book.sheet_by_index(index)
        # 获取合并的单元格
        merged = merge_cell(sheet)
        print(merged)
        # 获取sheet的行数（默认每一行就是一条用例）
        rows = sheet.nrows
        # 如果sheet为空，那么rows是0
        if rows:
            for row in range(rows):
                data = sheet.row_values(row)   # 单行数据
                for index, content in enumerate(data):
                    if merged.get((row, index)):
                        # 这是合并后的单元格，需要重新取一次数据
                        data[index] = sheet.cell_value(*merged.get((row, index)))
                # print(data)
if __name__ == "__main__":
    fn = 'D:\\TDQS\\新疆\\聂桂春\\Import\\jjsh.xlsx'
    fn = 'D:\\TDQS\\1iotqsgf.com\\qs_pcnp\\1.0.0\\business\\upload_files\\0bb47f67-8325-11e8-a538-001122334455.xls'
    fn = 'C:\\Users\\Administrator\\Downloads\\test.xlsx'
    # get_merged(fn)
    data = read_excel_as_merge(fn)
    for d in data:
        print(d)
    # xls = xlrd.open_workbook(r'D:\\TDQS\\新疆\\聂桂春\\Import\\tae_base_jjshhxx.xlsx')
    # # 获取目标EXCEL文件sheet名
    # print( xls.sheet_names())
    # sheet=xls.sheet_by_index(1)
    # sheet = xls.sheet_by_name(xls.sheet_names()[0])