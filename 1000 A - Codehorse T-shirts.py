#http://codeforces.com/problemset/problem/1000/A  Codehorses T-shirt
# Start:    Finish:     Duration:    Attempts:   4  Difficulty: 1200

n = int(input())
d =[]
for i in range(n):
    d.append(input())
e =[]
for i in range(n):
    e.append(input())
f=e.copy()
for i in range(0,len(f)):
    if f[i] in d and f[i] in e:
            d.remove(f[i])
            e.remove(f[i])
print(len(d))

