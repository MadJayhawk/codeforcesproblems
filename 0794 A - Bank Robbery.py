# https://codeforces.com/problemset/problem/794/A -  Bank Robbery
# Start: 7:13    Finish:  xx     Duration: xx   Attempts: 2    Difficulty: 900


a, b, c = list(map(int, input().split()))
n = int(input())
x = list(map(int, input().split()))
cnt = 0
for i in x:
    if i > b and i < c:
        cnt += 1
print(cnt)
