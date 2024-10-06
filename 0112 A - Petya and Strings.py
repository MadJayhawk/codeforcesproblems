# https://codeforces.com/problemset/problem/112/A -  Petya and Strings
# Start:    Finish:     Duration:    Attempts: 1    Difficulty: 900

a = input().lower()
b = input().lower()
if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)

