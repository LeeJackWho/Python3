import pandas as pd
import numpy as np

a=pd.Series([9,8,7,6])
#print(a)
'''结果
自动索引
0 9
1 8
2 7
3 6
dtype:int64 是NumPy中的数据类型
'''
d = pd.DataFrame(np.arange(10).reshape(2,5))
#print(d)
d1 = {'城市':['北京','上海','广州','深圳','沈阳'],
   '环比':[101.5,101.2,101.3,102.0,100.1],
   '同比':[120.7,127.3,119.4,140.9,100.1],
   '定基':[120.7,127.3,119.4,140.9,100.1]}
d = pd.DataFrame(d1,index=['c1','c2','c3','c4','c5'])
print(d)