# https://codeforces.com/problemset/problem/706/B -   Interesting drink
# Start:    Finish:     Duration:    Attempts:  6   Difficulty:  1100
from bisect import bisect
n = int(input())
f = list(map(int, input().split()))
f.sort()
q = int(input())
for j in range(q):
    c = int(input())
    print(bisect(f, c) )

    
    # k=list(itertools.takewhile(lambda x: x <= c, f))
    # print(len(k))

