# https://codeforces.com/contest/1051/problem/A -  Vasya and Password

n = int(input())
for i in range(n):
    a = list(input())
    r=[0]*len(a)
    for j in range(len(a)):
        if 65<=ord(a[j])<=90:
            r[j]=1
        elif 97 <= ord(a[j]) <= 122 :
            r[j]=0
        else:
            r[j]=2
    print()
    print(r)
    p=set(r)
    v=[]
    for i in range(3):
        if i not in p:
            v.append(i)
    print('---',v)
    c="aB6"
    for i in range(3):
        if r.count(i)>1:
            a[r.index(i)]=c[i]
    print(a)




    print(p)
    # T='uW2'
    #
    # for k in range(0,3):
    #     if r.count(k+1)==0:
    #         x=1
    #         while x<len(a):
    #             r.index(r[x])
    #             if r.count(r[x])>1:
    #                 r[x]=k+1
    #                 a[x]=T[k]
    #                 break
    #             x+=1
    # print("".join(a))


