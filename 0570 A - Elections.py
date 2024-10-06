# https://codeforces.com/problemset/problem/570/A -  Elections

# Difficulty: 1200

candidates, cities = list(map(int, input().split()))
dd = [0] * candidates
for i in range(cities):
    a = list(map(int, input().split()))
    t = max(enumerate(a), key=lambda x: x[1])[0]
    dd[t] += 1
r = max(enumerate(dd), key=lambda x: x[1])[0]
print(r + 1)
