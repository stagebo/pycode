import xlrd
'''
__target__ = 扩展excel表头
'''
def expand_header(data):
    header = [item[1].split('|') for item in data]
    hei = max([len(item) for item in header])
    for h in header:
        t = h[len(h)-1]
        x = len(h)
        for i in range(x,hei):
            h.append(t)
    return header


def _expand_table_header( data):
    header = [item[1].split('|') for item in data]
    hei = max([len(item) for item in header])
    for h in header:
        t = h[len(h) - 1]
        x = len(h)
        for i in range(x, hei):
            h.append(t)
    ret = []
    for i in range(0, hei):
        item = []
        for j in header:
            item.append(j[i])
        ret.append(item)
    return ret


def _get_header_merge_info(header_data):
    rg = []
    hd = header_data
    for hds in hd:
        print(hds)
    for i in range(1, len(hd)):
        for j in range(0, len(hd[0])):
            if hd[i][j] == hd[i - 1][j]:
                rg.append((i - 1, i, j, j))
    for i in range(0, len(hd)):
        for j in range(1, len(hd[0])):
            if hd[i][j] == hd[i][j - 1]:
                rg.append(( i, i,j - 1, j))

    return rg

if __name__ == "__main__":
    d = [['f_fl_yj', '基础信息分类|一级'], ['f_fl_ej', '基础信息分类|二级'], ['f_zhb', '指标'], ['f_shj', '数据']]
    hd = [['基础信息分类', '基础信息分类', '指标', '数据'], ['一级', '二级', '指标', '数据']]
    # hd = _expand_table_header(d)
    # print(hd)
    r = _get_header_merge_info(hd)
    print(r)