#http://codeforces.com/contest/1008/problem/B  Turn the Rectangles
def replace_at_index1(tup, ix, val):
    lst = list(tup)
    lst[ix] = val
    return tuple(lst)
n= int(input())
r=[]
for i in range(n):
    r.append(list(map(int,input().split())))
k=list(zip(*r))
print(k)
aa=k[0]
bb=k[1]
t=bb[0]
print(aa,bb)
for i in range(1,len(bb)):
    if t<bb[i]:
        bb=(replace_at_index1(bb,i,aa[i]))
print(bb)
t=bb[0]
sw=0
for i in range(1,len(bb)):
    if t>=bb[i]:
        t=bb[i]
        sw=1
    else:
        sw=0
        break
if sw==1:
    print("YES")
else:
    print("NO")
---------------------------------------------------------------------------------
# 10
# 706794178 103578427
# 431808055 641644550
# 715688799 406274173
# 767234853 345348548
# 241724251 408945969
# 808703176 213953908
# 185314264 16672343
# 553496707 152702033
# 105991807 76314740
# 61409204 244301685
----------------------------------------------------------------------------------
n=int(input())
x=10**9
cnt=0
for _ in[0]*n:
    w,h=sorted(map(int,input().split()))
    cnt+=1
    print(w,h,cnt,x)
    if h<=x:
        x=h
    else:
        if w<=x:
            x= w
        else:
            x=0
print(('NO','YES')[x>0])
-------------------------------------------------------------------------------------
n = int(input())
a = [input().split() for i in range(n)]

res = 'YES'
prv = 1234567890
for x in a:
    mn = min(int(x[0]), int(x[1]))
    mx = max(int(x[0]), int(x[1]))
    if prv < mn:
        res = 'NO'
    prv = mx if mx <= prv else mn

print(res)
------------------------------------------------------------------------------------
n=int(input())
a,fail=10**10,False
for i in range(n):
    if not fail:
        w,h=map(int,input().split())
        if max(w,h)<=a:
            a=max(w,h)
        elif min(w,h)<=a:
            a=min(w,h)
        else:
            fail=True
if fail==True:
    print("NO")
else:
    print("YES")
------------------------------------------------------------------------------------
x=[]
c=0
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    x.append([a,b])
y=[max(x[0])]
for i in range(1,n):
    if max(x[i])<=y[i-1]:
        y.append(max(x[i]))
    else:
        y.append(min(x[i]))
z=list(reversed(sorted(y)))
if y==z:
    print("YES")
else:
    print("NO")
-----------------------------------------------------------------------
By orailly, contest: Codeforces Round #497 (Div. 2), problem: (B) Turn the Rectangles, Accepted, #
 from sys import stdin


def main():
    r, H = bool(input()), 10 ** 9
    for s in stdin.read().splitlines():
        w, h = map(int, s.split())
        if h < w:
            h, w = w, h
        if H >= h:
            H = h
        elif H >= w:
            H = w
        else:
            r = False
            break
    print(('NO', 'YES')[r])


if __name__ == '__main__':
    main(
