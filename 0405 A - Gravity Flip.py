#https://codeforces.com/problemset/problem/405/A -  Gravity Flip
# Start:     Finish:     Duration:    Attempts: 4  Difficulty:  1000


def gravity_flip(m):
    return [str(i) for i in sorted(m)]
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(" ".join(gravity_flip(a)))