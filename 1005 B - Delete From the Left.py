#http://codeforces.com/contest/1005/problem/B
s=input()
t=input()
zab=(list(zip(s[::-1],t[::-1])))
d=0
for i in range(len(zab)):
    if zab[i][0]==zab[i][1]:
        d+=1
    else:
        break
print(len(s)+len(t)-2*d)
------------------------------------------------------------------------------
Input
abacabadabacaba
abacabadacaba
Answer
18
------------------------------------------------------------------------------
By linwe, contest: Codeforces Round #496 (Div. 3), problem: (B) Delete from the Left, Accepted, #
 import sys
import os

def test(str1, str2, n):
    return str2.endswith(str1[(len(str1) - n):])

def deleteFromLeft(str1, str2):
    n = min(len(str1), len(str2))
    if test(str1, str2, n):
        return abs(len(str1) - len(str2))

    left = 0
    right = n
    while right > left + 1:
        mid = (left + right) // 2
        if test(str1, str2, mid):
            left = mid
        else:
            right = mid

    return len(str1) + len(str2) - 2 * left

def main():
    str1 = input()
    str2 = input()
    print(deleteFromLeft(str1, str2))

if __name__ == '__main__':
    main()
------------------------------------------------------------------------------
By akjais, contest: Codeforces Round #496 (Div. 3), problem: (B) Delete from the Left, Accepted, #
 a = input()
b = input()
r = 0
for i in range(-1,-(min(len(a),len(b)))-1,-1):
    if a[i] != b[i]:
        r += 2
        break
r += len(b)+len(a) + i*2
print(r)
------------------------------------------------------------------------------
By Kiri11, contest: Codeforces Round #496 (Div. 3), problem: (B) Delete from the Left, Accepted, #
 s = input()
k = input()
r = len(s) + len(k)
for i, j in zip(reversed(s), reversed(k)):
    if i != j:
        break
    else:
        r -= 2

print(r)
------------------------------------------------------------------------------
By monkeywoora, contest: Codeforces Round #496 (Div. 3), problem: (B) Delete from the Left, Accepted, #
 a=input()
b=input()
c=int(len(a))
d=int(len(b))
f=int(0)
if c>=d:
	if d==1 and c==2:
		if b[-1]==a[-1]:
			print(int(1))
		else:
			print(int(3))
	else:
		for i in range(1,d+1):
			if a[-i]==b[-i]:
				f+=1
			elif a[-i]!=b[-i]:
				break
		print(int(int(c+d)-int(2*f)))
elif c<d:
	if c==1 and d==2:
		if a[-1]==b[-1]:
			print(int(1))
		else:
			print(int(3))
	else:
		for j in range(1,c+1):
			if a[-j]==b[-j]:
				f+=1
			elif a[-j]!=b[-j]:
				break
		print(int(int(c+d)-int(2*f)))
------------------------------------------------------------------------------


