# https://codeforces.com/contest/1016/problem/C  Vasya and the Mushrooms

# M = lambda: list(map(int,input().split()))
# # n = int(input())
# # 1st_row=[]
# # 2nd_row=[]
# # 1st_row.append(M())
# # 2nd_row.append(M())
# arr=[3,4,8,3,2,6,11,34]
# import pandas as pd
# data =list(pd.Series([1,6,5,2,3,4],index=[1,2,3,4,5,6]))
# print(data)
# for i in range(1,len(data)):
#     print(data[i])
# a=[[1,2,3,4,5,6],[1,6,5,2,3,4],[1,6,5,4,3,2],[1]]
# b = [x for x in range(0,6)]
# print(b)
# values=[]
# w=[]*6
# from itertools import *
# for i in zip(count(0), [1,2,3,4,5,6]):
#     print(i)
#
#
# print(values)
# j=[]
# for i in starmap(lambda x, y: (x, y, x * y), values):
#     j.append(i[2])
# print (sum(j))
from typing import List, Any, Union

a: List[Union[int, Any]]=[0,5,8,12,6,1,13]
for j in range(1,len(a)):
    k=a[j]
    i=j-1
    while i>=0 and a[i]>k:
        a[i+1]=a[i]
        i=i-1
    a[i+1]=k
print(a)

