# https://codeforces.com/problemset/problem/749/A -  Bachgold Problem
n = int(input())
print(n//2)
if n%2 == 0:
    print('2 '*(n//2))
else:
    print('2 '*(n//2-1)+'3')