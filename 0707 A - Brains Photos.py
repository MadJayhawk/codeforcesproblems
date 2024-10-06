# https://codeforces.com/contest/xxxx/problem/x -  Brains Photos
# Start:    Finish:     Duration:    Attempts:  4   Difficulty: 1000
n,m = list(map(int, input().split()))
ans = "#Black&White"
for i in range(n):
    r= input().split()
    if 'M' in r or 'Y' in r or 'C' in r:
        ans = '#Color'
        break
print(ans)

