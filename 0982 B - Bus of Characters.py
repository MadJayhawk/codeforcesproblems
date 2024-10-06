#http://codeforces.com/contest/982/problem/B
import time
# n= int(input())
# s= [int(n) for n in input().split()]
# c= input()
n= 6
s= [int(n) for n in "10 8 9 11 13 5".split()]
c= "010010011101"
u=[]
u=u+s
w=[]
d=dict()
for i in c:

    if i is '0':
        start=time.time()
        d=min(s)
        stop=time.time()
        print (u.index(d)+1,end=' ')
        w.append(d)
        del s[s.index(d)]

        print ('0  time: ',(time.time()-start)*10000)
    else:
        start=time.time()
        d=max(w)
        print(u.index(d)+1,end=' ')
        del w[w.index(d)]
        stop=time.time()
        print ('1  time: ',(time.time()-start)*10000)

# print('1 - ',i,s,' max: ',d,' list: ',t,' temp: ',w,' removed: ',e)
#n= 2
#s= [int(n) for n in "10 8 9 11 13 5".split()]
# c= "010010011101"
#s= [int(n) for n in "3 1".split()]
