'''
__target__ = 提取地图元件外包框
'''
import sys
def get_bbox( slist):
    coo = slist
    mina = sys.maxsize
    mino = sys.maxsize
    maxa = -sys.maxsize
    maxo = -sys.maxsize
    plist = []

    get_bbox_point(coo, plist)

    for item in plist:

        lat = float(item[0])
        lon = float(item[1])
        mina = min(mina, lat)
        mino = min(mino, lon)
        maxa = max(maxa, lat)
        maxo = max(maxo, lon)
        print(mina,mino,maxa,maxo,'---- ',lat,lon)
    bbox = [mina, mino, maxa, maxo]
    return bbox


def get_bbox_point( data, result):
    if isinstance(data, list) and len(data) == 2 and isinstance(data[0], (str, float,int)):
        result.append(data)
    elif isinstance(data, list):
        for item in data:
            get_bbox_point(item, result)


data = [[1,2],[1,2]]

x = get_bbox([46176.5078125, 858900.3125 ])
print(x)
# print(ret)
# print(x)
