# https://codeforces.com/contest/xxxx/problem/x -  name

def get_test_data():
    global n, m, s, t
    s = ['code*s', 'vk*cup', 'v', 'gfgf*gfgf']
    t = ['codeforces', 'vkcup', 'k', 'gfgfgf']
    n = [len(x) for x in t]
    m = len(s)


def get_problem_data():
    global n, m, s, t
    M = lambda: list(map(int, input().split()))
    n, m = M()
    s = input()
    t = input()


def solve(n, m, s, t):
    if '*' in s:
        l, r = s.split('*')
        return len(l) + len(r) <= len(t) and t.startswith(l) and t.endswith(r)
    else:
        return s == t


get_test_data()
for j in range(0, m):
    print(['NO', 'YES'][solve(n[j], m, s[j], t[j])])

# get_problem_data()
# print(['NO', 'YES'][solve(n, m, s, t)])
###########################################################################################
#By shailendra98k, contest: Manthan, Codefest 18 (rated, Div. 1 + Div. 2), problem: (A) Packets, Accepted, #
import math
n=int(input())
r=int((math.log(n,2)))
print(r+1)
##########################################################################################
#By Yee_172, contest: Manthan, Codefest 18 (rated, Div. 1 + Div. 2), problem: (A) Packets, Accepted, #
print(len(bin(int(input()))) - 2)
##########################################################################################
#By rhincodon66, contest: Manthan, Codefest 18 (rated, Div. 1 + Div. 2), problem: (A) Packets, Accepted, #
n = int(input())
ans = 0
a = 1
while n>0:
    ans+=1
    n-=a
    a*=2
print(ans)
##########################################################################################
#By Aditya_Ramesh, contest: Manthan, Codefest 18 (rated, Div. 1 + Div. 2), problem: (A) Packets, Accepted, #
'''
7 -> 1 2 4
6 -> 1 2 3
5 -> 1 1 3
4 -> 1 1 2
3 -> 1 2
2 -> 1 1
1 -> 1
'''
n = int(input())
ct = 0
while n!=0:
    n = n>>1
    ct += 1
print(ct)