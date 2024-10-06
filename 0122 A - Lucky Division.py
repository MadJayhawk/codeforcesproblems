# https://codeforces.com/problemset/problem/122/A -  Lucky Division
# Start: 7:51pm   Finish: 8:10    Duration: 19 minutes   Attempts: 3    Difficulty: 1000

a = input()
b = list(a)
for i in a:
    ans = "YES"
    if int(i) == 7 or int(i) == 4 or int(a) % 4 == 0 or int(a) % 7 == 0 or int(a) % 47 == 0:
        pass
    else:
        ans = "NO"
        break
print(ans)
