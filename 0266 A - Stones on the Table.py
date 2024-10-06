# https://codeforces.com/problemset/problem/266/A -  Stones on the Table
# Start: 10:14pm   Finish:10:24     Duration: 10 minutes   Attempts:  1   Difficulty:  800

n = int(input())
s = input()
h=s[0]
cnt=0
for i in range(1, n):
    if s[i] == h:
        cnt+=1
    else:
        h = s[i]
print(cnt)