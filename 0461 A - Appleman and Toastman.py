# https://codeforces.com/problemset/problem/461/A -  Appleman and Toastman

# Difficulty: 1200


def appleman_and_toastman(n, a):
    b = sorted(a)
    s = sum(b)
    t = s
    if n > 1:
        for i in range(n - 1):
            t += b[i]
            s -= b[i]
            t += s
    return t


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(appleman_and_toastman(n, a))
