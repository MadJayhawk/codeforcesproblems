# https://codeforces.com/contest/1020/problem/A New Building for SIS

# M = lambda: list(map(int,input().split()))
# n,h,a,b,k = M()
# ans=[]
# for i in range(0,k):
#     x1,y1,x2,y2= M()
#     q=range(a,b)
#     if x1==x2:
#         d = abs(y1 - y2)
#     else:
#         if y1 >= b:
#             d = abs(y1 - b)+abs(x1-x2)+abs(y2-b)
#         else:
#             d = abs(y1 - a)+abs(x1-x2)+abs(y2-a)
#     ans.append(d)
# for i in ans:
#     print(i)
n, h, a, b, k = [int(x) for x in input().split()]
for _ in range(k):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    res = abs(x1 - x2)
    if a <= y1 <= b or a <= y2 <= b or res == 0:
        res += abs(y1 - y2)
    else:
        res += min([abs(y1 - x) + abs(y2 - x) for x in [a, b]])
    print(res)