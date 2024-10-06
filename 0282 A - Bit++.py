# https://codeforces.com/problemset/problem/282/A -  Bit++
# Start:    Finish:     Duration: 10    Attempts:  1   Difficulty: 900
cnt=0
n = int(input())
for i in range(n):
    s = input()
    if '++' in s:
        cnt += 1
    if '--' in s:
        cnt -= 1
print(cnt)