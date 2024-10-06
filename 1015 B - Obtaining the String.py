#  https://codeforces.com/contest/1015/problem/B  Obtaining the String

n=int(input())
a=list(input())
b=list(input())
c=[]
t=0
s=0
try:
    while a!=b:
        for i in range(t,n-1):
            if a[i]==b[i]:
                pass
            else:
                if a[i+1]==a[i]:
                    pass
                else:
                    a[i+1],a[i]=a[i],a[i+1]
                    c.append(i+1)
        t=c[s]
        s+=1
    print (len(c))
    print (*c)
except:
    print(-1)
#------------------------------------------------------------------------------------------
#
#  import sys
# i=input
# n=int(i())
# s=[*i()]
# t=i()
# if sorted(s)!=sorted(t):
#  print(-1)
#  sys.exit()
# r=[]
# for i in range(n):
#  for j in range(i,n):
#   if s[j]==t[i]:
#    s[i:j+1]=s[j:j+1]+s[i:j]
#    r.extend(range(j,i,-1))
#    break
# print(len(r))
# print(*r)
# #------------------------------------------------------------------------------------------
# n = int(input())
# s = input()
# t = input()
# ans = list()
# if sorted(s) == sorted(t):
#     for i in range(n):
#         ind = s[i:].index(t[i]) + i
#         for j in range(ind - 1, i - 1, -1):
#             ans.append(j + 1)
#         s = s[:i] + t[i] + s[i:ind] + s[ind + 1:]
#     print(len(ans))
#     print(*ans)
# else:
#     print(-1)
# -----------------------------------------------------------------------------------------
# By eugalt, contest: Codeforces Round  # 501 (Div. 3), problem: (B) Obtaining the String, Accepted, #, hack it!
# n = int(input())
# s, t = [*input()], input()
# k = 0
# c = []
# try:
#     for i in range(n): j = s.index(t[i], i)
#         s[i], s[i + 1:j + 1] = s[j], s[i:j]\
#         k += j - i\
#         c += [*range(j, i, -1)]
# except:
#     print(-1)
# else:
#     print(k);print(*c)
# -----------------------------------------------------------------------------------------
# By Hi.Bitch, contest: Codeforces Round #501 (Div. 3), problem: (B) Obtaining the String, Accepted, #, hack it!
# import sys, math
# n = map(int, input())
# s = list(input())
# t = list(input())
#
# if sorted(s) != sorted(t):
#     print(-1)
#     sys.exit()
#
# a = []
# for k, c in enumerate(t):
#     i = s.index(c)
#     for j in reversed(range(1, i+1)):
#         a.append(j+k)
#     s.pop(i)
#
# print(len(a) or 0)
# print(' '.join(str(i) for i in a))