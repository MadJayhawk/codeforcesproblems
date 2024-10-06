# https://codeforces.com/contest/1025/problem/x -  Doggo Recoloring
def get_test_data():
    global n, m, s
    s = ["a", "abc", "aferfewrqvbgryhwtqtewrtqwertqwrqwerwqerwqerwerbgscgehrytretyj"]
    n = [len(x) for x in s]
    m = len(s)


def get_problem_data():
    global n, m, s
    M = lambda: list(map(int, input().split()))
    n = M()
    s = input()


def solve(s):
    b = len([s.count(x) for x in s if s.count(x) >= 2])
    print("Yes" if b > 0 or n == 1 else "No")


get_test_data()
for j in range(0, m):
    solve(s[j])

# get_problem_data()
# solve(s)
