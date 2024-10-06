# https://codeforces.com/problemset/problem/546/A -  Soldier and Bananas
# Start: 3:15am    Finish: 3:22am     Duration:  7 minutes  Attempts:  1   Difficulty: 800


k,n,w = list(map(int, input().split()))
s=0
for i in range(1,w+1):
    s += i*k
if s>n:
    print(abs(s-n))
else:
    print(0)
