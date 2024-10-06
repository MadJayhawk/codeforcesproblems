# https://codeforces.com/problemset/problem/237/A -  Free Cash

# Difficulty: 1200


def name_of_problem(n, a):
    d = [0] * 10000
    for i in range(n):
        h, m = a[i]
        d[h * 60 + m] += 1
    return max(d)


if __name__ == "__main__":
    nn = int(input())
    dd = []
    for i in range(nn):
        dd.append(list(map(int, input().split())))
    print(name_of_problem(nn, dd))
