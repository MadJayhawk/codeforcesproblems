#http://codeforces.com/contest/993/problem/A   Hit the Lottery  Rating:470
n =int(input())
m=[100,20,10,5,1]
cnt=0
for i in m:
    x=n//i
    n=n-x*i
    cnt=cnt+x
print(cnt)
-------------------------------------------------------------------------
SOLUTIONS
Input
79
Answer
9
-------------------------------------------------------------------------
By mukesh5, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (A) Hit the Lottery, Accepted, #
 n = int(input().strip())
l = [100,20,10,5,1]
count=0
i=0
while n>0:
	if l[i]<=n:
		tmp = n//l[i]
		count+=tmp
		n=n%l[i]
		i+=1

	else:
		i+=1

print(count)
-------------------------------------------------------------------------
By aslan_dukenbay, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (A) Hit the Lottery, Accepted, #
 n = int(input())
a = n // 100
n %= 100
b = n // 20
n %= 20
c = n // 10
n %= 10
d = n // 5
n %= 5
print(a + b + c + d + n)
-------------------------------------------------------------------------
By smureti, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (A) Hit the Lottery, Accepted, #
 def f(n):
    coins = [100, 20, 10, 5, 1]

    res = 0
    remaining = n
    for i in coins:
        a, b = divmod(remaining, i)
        remaining -= a * i
        res += a
        if b == 0:
            break

    return res

n = int(input())
print(f(n))
-------------------------------------------------------------------------
By denny_sem, contest: Codeforces Round #492 (Div. 2) [Thanks, uDebug!], problem: (A) Hit the Lottery, Accepted, #
 n = int(input())
a = [100,20,10,5, 1]
ans = 0
i = 0
while i < 5 and n > 0:
    if a[i] <= n:
        ans+=n//a[i]
        n %= a[i]
    else:
        i+=1
print(ans)
-------------------------------------------------------------------------
