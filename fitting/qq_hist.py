import numpy as np
import matplotlib.pyplot as plt

'''
__target__ = 直方图数据生成
'''

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
x = [1530.4,218.78,365,1445,1066,139.4,574.5,443.7,220.3,845.4,2583.1,922.4,1749.8
,229.6,1471.9,587.7,678.4,527.8,707.9,830,417.3,885.53,369,1554.91,521.48,1071.27
,675.54,579.78,909.61,867.86,330.42,222,680]

# 直方图

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()