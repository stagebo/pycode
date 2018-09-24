
'''
__target__ = Python assert 使用测试
'''
def division(a,b):
    assert b!=0,"除数不能为0"
    return a/b

def divisions(a,b):
    if b==0:
        raise AssertionError('除数不能为空')
    return a/b


if __name__ == "__main__":
    print(division(1,2))
    print(division(1,0))