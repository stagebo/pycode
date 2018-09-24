'''
__target__ = Pandas包测试
'''
import numpy as np
import pandas as pd

d = [{
    'a':1,
    'b':2
},{'b':3,'a':4}]
df = pd.DataFrame(d,['a','b'])
ls =  df.values.tolist()
print(ls)
