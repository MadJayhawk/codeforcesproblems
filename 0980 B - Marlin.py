#http://codeforces.com/contest/980/problem/B
#n,k=map(int,input().split())
n=11
k=6
s='.'*n
m=(k+1)//2
a='.'+'#'*m +'.'*(n-m-1)
# print(a)
if k%2<1:
    b=a
elif k<n:
    t=(n-k)//2*'.'
    b=t+'#'*k+t
else:
    b=a[:2]+'.'+a[3:]
print('YES',s,a,b,s,sep='\n')
# ---------------------------------------------------
#second solution
# ---------------------------------------------------
n, k = [int(x) for x in input().split()]

if k % 2 == 0:  # if k is even number print one # on lines 2 & 3 after first .
    print("YES")
    print("."*n)  # first line
    print("." + "#" * (k // 2) + "." * (n - 1 - k//2))  # second line  .#.....
    print("." + "#" * (k // 2) + "." * (n - 1 - k//2))  # third line
    print("."*n)        # fourth line
elif n % 2 == 1:  # if k is odd number print a number of #s on lines 2 & 3 after first .
    print("YES")
    print("."*n)
    top = min(k, n-2)
    bot = (k - top)
    print("." * ((n - top) // 2) + "#" * top + "." * ((n - top) // 2))
    print("." + "#" * (bot // 2) + "." * (n - 2 - bot) + "#" * (bot // 2)  + ".")
    print("."*n)
else:
    print("NO")
