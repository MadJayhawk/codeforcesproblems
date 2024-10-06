# https://codeforces.com/contest/xxxx/problem/x -  name

def get_test_data():
    global n, m, s
    s = ['1 2 5 6 7 10 21 23 24 49', '2 10 50 110 250', '4 7 12 100 150 199']
    n = [len(x) for x in s]
    m = len(s)


def get_problem_data():
    global n, m, s, t
    M = lambda: list(map(int, input().split()))
    n, m = M()
    s = input()
    t = input()


def solve(nn, mm, ss ):
    ans=3*nn
    return ans


get_test_data()
for j in range(0, m):
    print(solve(n[j], m, s[j]))

# get_problem_data()
# print(['NO', 'YES'][solve(n, m, s, t)])