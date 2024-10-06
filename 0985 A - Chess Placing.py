#http://codeforces.com/contest/985/problem/A  Chess Placing
n = int(input())
p = sorted(map(int, input().split()))

b = 0
w = 0

for i, pi in enumerate(p):
    b += abs(pi - (2 * i + 1))
    w += abs(pi - (2 * i + 2))

print(min(b, w))
# n=int(input())
# p=[int(i) for i in input().split()]
# b=[]
# a=[]
# t=0
# cnt=0
# for i in range (0,n):
#     b.append(0)
# for i in range(0,len(p)):
#     b[p[i]-1]=1
# print (b,p)
# g=int(n/2)
# cnt=1
# for i in range(0,g):
#     a.append(1)
#     a.append(0)
#     cnt+=2
# print (a,b)
#
# cnt=0
# for i in range(0,n):
#     print (b[i],a[i],b.index(0))
#     if b[i]==a[i]:
#         continue
#     elif b[i]==1 and a[i]==0:
#         b[i]=0
#         cnt+=1
#     elif b[i]==0 and a[i]==1:
#         b[i]=1
#         cnt+=1
# print(cnt,b,a)
