# https://codeforces.com/problemset/problem/71/A -  Way Too Long Words

n = int(input())
c=[]
for i in range(n):
    s = input()
    if len(s) > 10:
        w = s[0]+str(len(s)-2)+s[-1]
    else:
        w = s
    c.append(w)
for i in c:
    print(i)
