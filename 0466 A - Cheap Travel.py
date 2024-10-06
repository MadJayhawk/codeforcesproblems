# https://codeforces.com/problemset/problem/466/A -  Cheap Travel
# Start:    Finish:     Duration:    Attempts: 6    Difficulty: 1200

def cheap_travel(n, m, a, b):
    d=[]
    d.append((n//m)*b + (n%m)*a)
    d.append(((n // m)+1) * b )
    d.append(n*a)
    return min(d)

# --------------------------------------------------------------
if __name__ == '__main__':
    f = lambda: list(map(int, input().split()))
    n, m, a, b = f()
    print(cheap_travel(n, m, a, b))

