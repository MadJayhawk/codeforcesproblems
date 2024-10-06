# https://codeforces.com/problemset/problem/977/C -  Less or Equal

# Difficulty: 1200


def less_or_equal(n, k, a):
    if k == 0:
        if a[0] > 1:
            return 1
        else:
            return -1
    else:
        if k == n or a[k] > a[k - 1]:
            return a[k - 1]
        else:
            return -1


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    aa = sorted(list(map(int, input().split())))
    print(less_or_equal(n, k, aa))
