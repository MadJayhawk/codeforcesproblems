# https://codeforces.com/problemset/problem/445/A -  DZY Loves Chessboard

# Difficulty:  1200


def dzy_loves_chessboard(n, m, d):
    p = "W"
    b = "W"
    for i in range(n):
        for j in range(m):
            if d[i][j] == ".":
                d[i][j] = p
            if p == "W":
                p = "B"
            else:
                p = "W"
        if b == "W":
            b = "B"
            p = "B"
        else:
            b = "W"
            p = "W"
    return d


if __name__ == "__main__":
    nn, mm = list(map(int, input().split()))
    dd = []
    for i in range(nn):
        dd.append(list(input()))
    z = dzy_loves_chessboard(nn, mm, dd)
    for i in z:
        print("".join(i))

"""
3 8
..--...-
.---..--
...-.-..

"""
