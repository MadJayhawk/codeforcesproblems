# https://codeforces.com/problemset/problem/456/A -  Laptops
# Start:    Finish:     Duration:    Attempts:     Difficulty: 1200


def laptops(x, y):
    if x != y:
        return "Happy Alex"
    return "Poor Alex"


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        if a != b:
            print("Happy Alex")
            exit()
    print("Poor Alex")
