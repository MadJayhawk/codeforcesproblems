# https://codeforces.com/problemset/problem/421/A -  Pasha and Hamsters
# Start:    Finish:     Duration: ~20 minutes   Attempts: 1     Difficulty: 800

n, a, b = list(map(int, input().split()))
h = list(map(int, input().split()))
x = list(map(int, input().split()))
c = ['0']*(n+1)
for i in h:
    if i not in c:
        c[i]='1'
    else:
        c[i]='2'
for i in x:
    if i not in c and c[i] == '0':
        c[i] ='2'
print(" ".join(c[1:]))
    