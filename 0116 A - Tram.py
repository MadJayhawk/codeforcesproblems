# https://codeforces.com/problemset/problem/116/A -  Tram
# Start: 10:47    Finish: 11:08    Duration: 21  Attempts:1    Difficulty: 800

n = int(input())
c = 0
t =[]
for i in range(n):
    a, b = list(map(int, input().split()))
    c=c-a+b
    t.append(c)
print(max(t))
