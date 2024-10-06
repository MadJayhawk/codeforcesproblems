#   http://codeforces.com/contest/978/problem/A
n= int(input())
#n=6
c= input()
#c="1 5 5 1 6 1"
a=c.split()
a.reverse()
b=[]
for i in range(0,n):
    if a[i] in a and a[i] not in b:
        b.append(a[i])
b.reverse()
print (len(b))
for i in b:
    print (i, end=' ')
    if i==len(b):
        print()
