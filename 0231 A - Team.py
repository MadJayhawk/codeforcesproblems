# https://codeforces.com/problemset/problem/231/A -  Team
# Start: 10:46    Finish:  10:51   Duration: 5  Attempts: 1  Difficulty:  800

n = int(input())
cnt = 0
for i in range(n):
    a = list(map(int, input().split()))
    if a.count(1)>=2:
        cnt+=1
print(cnt)
