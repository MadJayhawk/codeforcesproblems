# https://codeforces.com/problemset/problem/492/B -  Vanya and Lanterns
# Start:    Finish:     Duration:    Attempts: 2    Difficulty: 1200

def vanya_and_lanterns(s, r):
    a = sorted(r)
    b = [(a[i + 1] - a[i])/2 for i in range(len(a) - 1)]
    b.append(a[0])
    b.append(d-a[-1])
    return max(b)

# --------------------------------------------------------------
if __name__ == '__main__':
    f = lambda: list(map(int, input().split()))
    n, d = f()
    b = f()
    print(vanya_and_lanterns(d, b))

