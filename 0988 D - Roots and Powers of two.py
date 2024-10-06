#http://codeforces.com/contest/988/problem/D Points and Powers of Two
def iroot(k, n):  #Newton's method
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s
def nth_root(n, k):
    x = n**(1./k)
    y = int(x)
    return y + 1 if y != x else y
print (iroot(2,32))
print(nth_root(2,2))
