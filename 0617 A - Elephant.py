# https://codeforces.com/problemset/problem/617/A-  Elephant  (700 difficulty)
# start: 10:53    complete: 11:01    No of submissions: 3
x = int(input())
if x <= 5:
    a=1
elif x%5==0:
    a = x//5
else:
    a = x//5 + 1
print(a)
