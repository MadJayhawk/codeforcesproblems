# https://codeforces.com/contest/1023/problem/B -  Pair of Toys


def get_test_data():
    global n, k, m
    # n = [1000000000000, 8, 8, 7]
    # k = [1000000000001, 5, 15, 20]
    n = [8, 8, 7]
    k = [5, 15, 20]

    m = len(n)


def get_problem_data():
    global n, k
    M = lambda: list(map(int, input().split()))
    n, k = M()


def solve(a, b):
    """
        a=# of toys for sale  k=total cost
        (a,b) = (b,a)
        a != b
        a>=1, b <= 10**14
    """
    d = (b // 2) + 1
    print("----", a, b, d)
    ans = 0

    for i in range(d, 1, -1):
        print(b - i, i, b, b - i <= a)
        if b - i <= a:
            ans += 1
    return ans


get_test_data()
for j in range(0, m):
    print(solve(n[j], k[j]))

# get_problem_data()
# print(['NO', 'YES'][solve(n, m, s, t)])
