#http://codeforces.com/contest/998/problem/0 - Balloons
n=int(input())
p=list(map(int,input().split()))
mn= min(p)
inxMn=p.index(mn)
mx=max(p)
a=[]
if mn==mx or n==1:
    print ('-1')
else:
    del p[inxMn]
    for i in p:
        a.append(i)
    print (len(a))
    for i in a:
        print(i,end=" ")

NOT CORRECT  Stops at Problem Set #5
10
1 1 1 1 1 1 1 1 1 1
------------------------------------------------------------------------------------------------
# Input
# 6
# 108 318 583 10 344 396
#
# Answer
# 1
# 4
------------------------------------------------------------------------------------------------
#By pyrus, contest: Codeforces Round #493 (Div. 2), problem: (A) Balloons, Accepted, #
 #!/usr/bin/env python3

n = int(input().strip())
a = list(map(int, input().strip().split()))

if n < 2 or (n == 2 and a[0] == a[1]):
    print (-1)
else:
	print (1)
	print (a.index(min(a)) + 1)
------------------------------------------------------------------------------------------------

n = int(input())
a = list(map(int, input().split()))

if len(a) == 1:
	print(-1)
elif len(a) == 2 and a[0] == a[1]:
	print(-1)
else:
	mina = min(a)
	for i, x in enumerate(a):
		if x == mina:
			print(1)
			print(i + 1)
			break
------------------------------------------------------------------------------------------------
By Sushant00, contest: Codeforces Round #493 (Div. 2), problem: (A) Balloons, Accepted, #
 from math import ceil

t = 1
for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n==1:
        print(-1)
        continue
    minval = 2000
    minInd = -1
    ind = 0
    for i in a:
        if i<minval:
            minval = i
            minInd = ind
        ind+=1
    if sum(a)-minval == minval:
        print(-1)
    else:
        print(1)
        print(minInd+1)
------------------------------------------------------------------------------------------------
By nethish, contest: Codeforces Round #493 (Div. 2), problem: (A) Balloons, Accepted, #
 # import sys
# sys.stdin=open('F:\\C\\Script\\input.txt','r')
# sys.stdout=open('F:\\C\\Script\\output.txt','w')
# sys.stdout.flush()

n = int(input())
l = [int(i) for i in input().split()]
s = sorted(l)

if n == 1 :
	print (-1)
elif s[0] != sum(s[1:]):
	print (1)
	print (l.index(s[0])+1)
else:
	print (-1)

------------------------------------------------------------------------------------------------
By Megatvini, contest: Codeforces Round #493 (Div. 2), problem: (A) Balloons, Accepted, #
 # http://codeforces.com/contest/998/problem/0

import itertools


def find_subsets(nums):
    for m in range(len(nums)):
        for subset in itertools.combinations(nums, m):
            yield subset


def read_nums():
    return [int(x) for x in input().split()]


def main():
    n, = read_nums()
    balloons = read_nums()
    if len(balloons) == 1:
        print(-1)
        return

    total_sum = sum(balloons)
    balloons = list(enumerate(balloons))
    for subset in find_subsets(balloons):
        if len(subset) > 0 and sum([x[1] for x in subset]) * 2 != total_sum:
            print(len(subset))
            print(' ' .join([str(index + 1) for index, num in subset]))
            return
    print(-1)


if __name__ == '__main__':
    main()
------------------------------------------------------------------------------------------------