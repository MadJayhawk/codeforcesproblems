#http://codeforces.com/contest/988/problem/C  Equal Sums
k=[]
a=[]
xx=[]
n=2
t=[5,6]
v=['2 3 1 3 2','1 1 2 2 2 1']
for i in range(n):
    k.append(t[i])
    a.append(list(map(int,v[i].split())))
# n=int(input())
# for i in range(n):
#     k.append(int(input()))
#     a.append(list(map(int,input().split())))
for y in range(0,n-1):
    for w in range(y+1,n):
        sa=a[y]
        sb=a[w]
        d=abs(sum(a[y])-sum(a[w]))  #s.append(sum(map(int,i.split())))# sums of sequences
        cnt=0
        c=''
        for p in range(k[y]):
            for q in range(k[w]):
                if d == abs(sa[p]-sb[q]):
                    c="Yes"
                    xx.append(str(p+1)+" "+str(q+1))
                    xx.append(str(q+1)+" "+str(p+1))
                    print (xx,d,sa[p],sb[q])
                        # for r in range(k[w]):
                        #     for s in range(k[y]):
                        #         if d == abs(sb[r]-sa[s]):
                        #             c="Yes"
                        #                 xx.append(str(s+1)+" "+str(r+1))

                #     cnt=cnt+1
                #     if cnt == 2:
                #         break
                # else:
                #     continue
                # break # breaks second loop
if c=="Yes":
    print ("Yes")
    for aa in range(0,len(xx)):
        print (xx[aa])
else:
    print ("No")
# n=2
# t=[5,6]
# v=['2 3 1 3 2','1 1 2 2 2 1']
# for i in range(n):
#     k.append(t[i])
#     a.append(v[i])
