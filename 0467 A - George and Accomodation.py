# https://codeforces.com/problemset/problem/467/A -  George and Accomodation
# Start: 9:39am   Finish: 9:45am    Duration:  6 minutes  Attempts:  1   Difficulty: 800

n = int(input())
cnt=0
for i in range(0,n):
    p,q = list(map(int, input().split()))
    if p+2>q:
        pass
    else:
        cnt+=1
print(cnt)
