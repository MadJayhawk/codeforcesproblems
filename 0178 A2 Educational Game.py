# https://codeforces.com/contest/178/problem/A2 -  Educational Game
# Start:    Finish:     Duration:    Attempts: 3    Difficulty: 1000
def educational_game(m, b):
    c = 0
    for i in range(m - 1):
        t = 0
        while (i + (1 * 2 ** t)) < m:
            t += 1
        j = i + (1 * 2 ** (t - 1))
        b[j] += b[i]
        c += b[i]
        print(c)
# --------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    educational_game(n,a)
    