# https://codeforces.com/problemset/problem/474/B -  Worms

# Difficulty:  1300


def worms(n, a, m, q):
    b = []
    c = 0
    qq = sorted(q)
    c = 0
    B = (i + c for i in a)
    print(list(B))
    for i in a:
        c += i
        b.append(c)
    i = 0
    G = ([x + 1, y] for x, y in enumerate(b))
    for i in qq:
        v = next(G)
        if v[1] > i:
            print(v[0], v[1])
            v = next(G)
        # for x, y in enumerate(b):
        #     if y >= i:
        #         print(x + 1)
        #         break
        # print(next(x + 1 for x, y in enumerate(b) if y >= i))


if __name__ == "__main__":
    I = lambda: list(map(int, input().split()))
    n = I()[0]
    a = I()
    m = I()[0]
    q = I()
    t = worms(n, a, m, q)
