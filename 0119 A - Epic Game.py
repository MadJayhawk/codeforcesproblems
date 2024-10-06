# https://codeforces.com/contest/xxxx/problem/x -  name
# Start:     Finish:     Duration:    Attempts: 7  Difficulty:  1000

from math import gcd
def epic_game(a, b, n):
    # d = {a: 0, b: 1}
    d=1
    e=0
    while True:
        n -= gcd(a, n)
        if n == 0:
            break
        a, b = b, a
        d, e = e, d
    return e
# --------------------------------------------------------------
if __name__ == '__main__':
    # f = lambda: map(int, input().split())
    # a, b, n = f()
    # print(epic_game(a, b, n))
    aa = '100 100 100'
    f = lambda: map(int, aa.split())
    a, b, n = f()
    print(epic_game(a, b, n))
    aa = '10 10 3'
    f = lambda: map(int, aa.split())
    a, b, n = f()
    print(epic_game(a, b, n))
# --------------------------------------------------------------
def gcd(a,b):
    while (a):
        b%=a
        a,b=b,a
    return b

def main():
    x,y,n=map(int,input().split())
    i=0
    while(n):
       if  not i%2:
           n-=gcd(x,n)
       else:
           n-=gcd(y,n)
       i+=1
    print(int(not i%2))
main()
