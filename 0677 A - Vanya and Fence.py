# https://codeforces.com/problemset/problem/677/A - Vanya and Fence
# Start  9:27pm    Finish 9:36     Duration  9 minutes   Difficulty:  700

b = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = b[0]
for i in a:
    if i > b[1]:
        cnt+=1
print(cnt)





