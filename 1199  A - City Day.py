# https://codeforces.com/contest/1199/problem/0 -  City Day

# Difficulty:


def city_day(n, s, a, b):
    for i in range(n):
        y = s[max(0, i - a) : min(i + b + 1, n)]
        target = s[i]
        y.sort()
        if y[0] == target:
            return i + 1


if __name__ == "__main__":
    n, r, t = list(map(int, input().split()))
    v = list(map(int, input().split()))
    print(city_day(n, v, r, t))
