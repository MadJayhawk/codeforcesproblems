# https://codeforces.com/problemset/problem/577/A -  Multiplication Table
# Start:    Finish:     Duration:    Attempts: 2    Difficulty: 1100

def multiplication_table(n, x):
    a = [v+1 for v in range(n) if x%(v+1)==0]
    return len([(r, s) for r in a for s in a if (r * s) == x])
# --------------------------------------------------------------
if __name__ == '__main__':
    f = lambda: map(int, input().split())
    m,y = f()
    print(multiplication_table(m, y))

    # m, y = [10,5]
    # print(multiplication_table(m, y))
    # m, y = [6, 12]
    # print(multiplication_table(m, y))
    # m, y = [5, 13]
    # print(multiplication_table(m, y))