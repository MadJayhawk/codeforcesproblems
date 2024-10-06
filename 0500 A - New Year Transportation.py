# https://codeforces.com/contest/xxxx/problem/x -  New Year Transportation
# Start:    Finish:     Duration:    Attempts:     Difficulty: 1100

def new_year_transportation(m, s, b):
    p = 1
    while p < t:
        p += b[p - 1]
    if p == t:
        return "YES"
    else:
        return "NO"

# --------------------------------------------------------------
if __name__ == '__main__':
    f = lambda: map(int, input().split())
    n,t = f()
    a = list(f())
    print(new_year_transportation(n, t, a))

