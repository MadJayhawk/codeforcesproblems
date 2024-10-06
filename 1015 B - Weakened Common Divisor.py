# https://codeforces.com/contest/1025/problem/x -  Weakened Common Divisor
def get_test_data():
    global n, m, s, t
    s = ['code*s', 'vk*cup', 'v', 'gfgf*gfgf']
    t = ['codeforces', 'vkcup', 'k', 'gfgfgf']
    n = [len(x) for x in t]
    m = len(s)


def get_problem_data():
    global n, m, s, t
    M = lambda: list(map(int, input().split()))
    n, m = M()
    s = input()
    t = input()


def solve(n, m, s, t):
    if '*' in s:
        l, r = s.split('*')
        return len(l) + len(r) <= len(t) and t.startswith(l) and t.endswith(r)
    else:
        return s == t


get_test_data()
for j in range(0, m):
    print(['NO', 'YES'][solve(n[j], m, s[j], t[j])])

# get_problem_data()
# print(['NO', 'YES'][solve(n, m, s, t)])