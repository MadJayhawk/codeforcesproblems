# https://codeforces.com/problemset/problem/236/A -  Boy or Girl
# Start: 2:42am   Finish: 2:58     Duration: 16   Attempts:  3   Difficulty: 800

s = input()
t = []*26
for i in s:
    if i in t:
        pass
    else:
        t.append(i)

if len(t)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
