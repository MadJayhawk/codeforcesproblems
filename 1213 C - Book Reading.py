# https://codeforces.com/problemset/problem/1213/C-  Book Reading

# Difficulty:1200


def book_reading(a, b):
    sum = 0
    for g in range(a):
        if g % b == 0:
            sum += str(g)[-1]
    return sum


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        n, m = list(map(int, input().split()))

        print(book_reading(n, m))
