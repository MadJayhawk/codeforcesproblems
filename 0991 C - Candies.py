#http://codeforces.com/contest/991/problem/C  -  Candies

import math
c=int(input())
d=int(c)
e=round(c/2+.5)
a=[]
t=d

cnt=0
b=[]
for k in range(1,c):
    for i in range(d,e,-1):
        a.append(t)
        print(-k,-math.floor(.1*t),-k-math.floor(.1*t),a)
        t=t+(-k-math.floor(.1*t))
        print (i,t,e)
        if t<e :
            break
        else:
            cnt+=1
    b.append(cnt)
    print ('----- ',b)
    a.clear()
    cnt=0
    t=d
-------------------------------------------------------------------------------------------------------------
SOLUTIONS
Input
756
Answer
29
-------------------------------------------------------------------------------------------------------------
By Pedantic, contest: Codeforces Round #491 (Div. 2), problem: (C) Candies, Accepted, #
 from math import ceil

def find_n(k):
    ev = n
    od = ev - k
    ev = od - od // 10
    c = 0
    while 1:
        c += 1
        od = ev - k # u_{2n + 1}
        if od < 0: return (c - 1 + 1) * k + ev
        ev = od - od // 10 # u_{2n + 2}


n = int(input())

a = 1
b = n // 2 + 1

while a <= b:
    k = (a + b) // 2
    if find_n(k) >= (n + 1) // 2:
        b = k - 1
        answer = k
    else:
        a = k + 1

print(answer)
-----------------------------------------------------------------------------------------------------------------------
By wfe2017, contest: Codeforces Round #491 (Div. 2), problem: (C) Candies, Accepted, #
 def greater(nowcandy, x):
	vas = int(0)
	pet = int(0)
	while nowcandy > 0:
		if nowcandy > x:
			nowcandy = nowcandy - x
			vas = vas + x
		else:
			vas = vas + nowcandy
			nowcandy = 0
		pet = pet + int(nowcandy // 10)
		nowcandy = nowcandy - int(nowcandy//10)
	if vas >= pet:
		return True
	else:
		return False

candies = int(input())

lo = int(1)
hi = int(candies)

while lo < hi:
	mid = int((lo + hi) // 2)
	if greater(candies, mid):
		hi = mid
	else:
		lo = mid + 1
print(lo)
-----------------------------------------------------------------------------------------------------------------------
By zelenoff4, contest: Codeforces Round #491 (Div. 2), problem: (C) Candies, Accepted, #
 n = int(input())
left = 1
right = n

def modulate(k):
    e = n
    Vasya = 0
    Petya = 0
    while e > 0:
        #print(e)
        if e <= k:
            Vasya += e
            break
        diff = e - k
        Vasya += k
        e -= k
        if e >= 10:
            Petya +=  diff // 10
            e -= diff // 10
        #print(e, ' left')
    #print(Vasya, 'ate Vasya overall')
    #print(Petya, 'ate Petya overall')
    if Vasya >= Petya:
        return True
    else:
        return False

while right - left > 1:
    middle = (right + left) // 2
    if not modulate(middle):
        left = middle
    else:
        right = middle

if modulate(left):
    print(left)
else:
    print(right)
--------------------------------------------------------------------------------------------------
By sergovoy, contest: Codeforces Round #491 (Div. 2), problem: (C) Candies, Accepted, #
 n = int(input())


def check(p):
    V = 0
    n_ = n
    while n_ > 0:
        temp = min(n_, p)
        V += temp
        n_ -= temp
        n_ -= n_ // 10

    return 2 * V >= n


def binSearch(a, b):
    left, right = a - 1, b + 1

    while right - left > 1:
        mid = (left + right) // 2

        if check(mid):
            right = mid

        else:
            left = mid

    return right


print(binSearch(1, n // 2))
