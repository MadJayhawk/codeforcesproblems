# https://codeforces.com/problemset/problem/349/A -  Cinema Line

# Difficulty: 1200


def cinema_line(x):
    a = {25: 0, 50: 0}
    ans = "YES"
    for i in x:
        a[i] += i
        if i != 25:
            if i == 50:
                if a[25] > 0:
                    a[25] -= 25
                else:
                    ans = "NO"
            if i == 100:
                if a[25] > 0 and a[50] > 0:
                    a[25] -= 25
                    a[50] -= 50
                elif a[25] > 50:
                    a[25] -= 75
                else:
                    ans = "NO"
    return ans


if __name__ == "__main__":
    n = int(input())
    b = list(map(int, input().split()))
    print(cinema_line(b))
