# -*- coding:utf-8 -*-
# Author : Mr Zhou
# Date : 2019/08/21

import requests
import csv 
import matplotlib.pyplot as plt

res = requests.get("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
print(type(res.text))
print(type(res.content))
print(type(res.content.decode('utf-8')))
lines = res.text.strip().split('\n')
print(type(lines))
x = []
y = []
for iline in lines:
    ilines = iline.split(';')
    x.append(ilines[0])
    y.append(ilines[1])
xlabel = [i for i in range(len(x)-1000)]
plt.plot(xlabel,y)
plt.show()

