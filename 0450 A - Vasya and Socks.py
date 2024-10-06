# https://codeforces.com/problemset/problem/460/A -  Vasya and Socks
def vasya_and_socks(f, s):
    h = 0
    while f!=0:
        h += 1
        f -= 1
        if f == 0 and h % s != 0:
            return h
        if h % s == 0:
            f += 1
# --------------------------------------------------------------
if __name__ == '__main__':
    f = lambda: map(int, input().split())
    n,m = f()
    print(vasya_and_socks(n,m))
    
    # n, m = [15, 30]
    # print(vasya_and_socks(n, m))
    # n, m = [9, 3]
    # print(vasya_and_socks(n, m))
# --------------------------------------------------------------

a,b=map(int,input().split())
print((a-1)//(b-1)+a)


# --------------------------------------------------------------
def main():
    n,m = read()
    i = 0
    while n:
        n -= 1
        i += 1
        if not i%m: n += 1
    print(i)

def read(mode = 2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))

def write(s = "\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end = "")

write(main())
# --------------------------------------------------------------
n, m = map(int, input().split())
day = 1
while n > 0:
    n -= 1
    if day % m == 0:
        n += 1
    day += 1

print(day - 1)