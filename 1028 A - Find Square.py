# https://codeforces.com/contest/xxxx/problem/x -  name

M = lambda: list(map(int, input().split()))
n, m = M()
d=[]
row=1
for i in range(0,n):
    b=input()
    col=b.find("B")
    if col !=-1:
        
        num_B = b.count("B")//2
        col = col + 1+num_B
        row=row+num_B
        
        break
    row+=1
print(row,col)
# row=1
# for i in d:
#     x=i.find("B")
#     if x != -1:
#         break
#     row+=1
# print(row,x+1,)


