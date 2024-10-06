# https://codeforces.com/contest/1185/problem/B -  Email from Polycarp
# Start:    Finish:     Duration:    Attempts:     Difficulty:

def email_from_polycarp(a, b):
    c = 0
    if len(b) >= len(a) and set(a) == set(b):
        for i in range(0, len(a)):
            while a[i] == b[c]:
                c += 1
                if c == len(b):
                    break
        if len(b) == c:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'
# --------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        r = input()
        s = input()
        print(email_from_polycarp(r, s))


