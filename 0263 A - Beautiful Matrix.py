# https://https://codeforces.com/problemset/problem/263/A -  Beautiful Matrix
# 12:20am - 12:56am    36min  First attempt
d = []
for i in range(5):
    d.append(list(map(int,input().split())))
for indx,i in enumerate(d):
    if i.count(1) >0:
        print(abs(indx-2)+abs(i.index(1)-2))



