# https://codeforces.com/problemset/problem/46/A -  Ball Game
# Start: 8:06pm   Finish:     Duration: Long time    Attempts: 2    Difficulty: 900  (HAD TO LOOK AT OTHER ANSWERS)
n = int(input())
children = 0
d = []
for i in range(1,n):
    children = (children+i)%n
    print(children + 1, end=' ')
