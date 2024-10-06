# http://codeforces.com/contest/1006/problem/B  Polycarps Practice

MIS = lambda: list(map(int,input().split()))
n, k = MIS()
a =  MIS()

a=sorted(zip(a,range(n)))[-k:] #[(5, 4), (6, 3), (9, 6)]
sm=sum(x[0]for x in a)
print(sm)  # 20
b=sorted(x[1]for x in a)  #[3, 4, 6]
# print(b[1:],b[2:]+[n],list(zip(b[1:],b[2:]+[n])))
if k>1:
    print(b[1],*(y-x for x,y in zip(b[1:],b[2:]+[n])))

NOT SUBMITTED
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
By eugalt, contest: Codeforces Round #498 (Div. 3), problem: (B) Polycarp's Practice, Accepted, #
 R=lambda:map(int,input().split())
n,k=R()
a=sorted(zip(R(),range(n)))[-k:]
print(sum(x[0]for x in a))
b=sorted(x[1]for x in a)+[n]
b[0]=0
print(*(y-x for x,y in zip(b,b[1:])))
------------------------------------------------------------------------------------
By kannappan, contest: Codeforces Round #498 (Div. 3), problem: (B) Polycarp's Practice, Accepted, #
 n,k=list(map(int, input().split(' ')))
a=list(map(int, input().split(' ')))


res=sorted(sorted(range(len(a)), key=lambda i: a[i])[-k:])
# print(res)
r1=0
r2=[]
tmp=-1
for i in res:
    r1+=a[i]
    r2.append(i-tmp)
    tmp=i
if k>1: r2[-1]=(n-1-res[-2])
if k==1: r2=[n]
print(r1)
print(*r2)
------------------------------------------------------------------------------------
By
m77, contest: Codeforces
Round  # 498 (Div. 3), problem: (B) Polycarp's Practice, Accepted, #


def main():
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    aa = [i for i in range(n)]
    aa.sort(key = lambda x: a[x], reverse = True)
    aa = aa[0:k]
    aa.sort()
    s = 0
    for e in aa:
        s += a[e]
    print(s)
    if k > 1:
        r = [aa[1]]

        for e in range(2, k):
            r.append(aa[e] - aa[e - 1])
        r.append(n - aa[len(aa) - 1])

        print(' '.join(map(str, r)))
    else:
        print(n)


main()
------------------------------------------------------------------------------------
By knight_coder, contest: Codeforces Round #498 (Div. 3), problem: (B) Polycarp's Practice, Accepted, #
 n,k=map(int,input().split())
s=list(map(int,input().split()))
sl=s[::]
sl.sort()
sl.reverse()
p=sl[0:k]
m=sum(p)
vall=[ 0 for i in range(2005) ]
for i in p:
    vall[i]+=1
sl=[]
t=0
for i in range(n):
    if vall[s[i]]>=1:
        sl+=[i+1]
        vall[s[i]]-=1
summ=0
for i in range(0,k):
    sl[i]=sl[i]-summ
    summ+=sl[i]
if sum(sl)<n:
    sl[k-1]+=n-sum(sl)
print(m)
sll=""
for i in sl:
    sll+=str(i)+" "
print(sll)
------------------------------------------------------------------------------------

