#http://codeforces.com/contest/988/problem/A   Diverse Team
s = input().split()
# s = "100 53".split()
n=int(s[0])
k=int(s[1])
r= input().split()
# r= "16 17 1 2 27 5 9 9 53 24 17 33 35 24 20 48 56 73 12 14 39 55 58 13 59 73 29 26 40 33 22 29 34 22 55 38 63 66 36 13 60 42 10 15 21 9 11 5 23 37 79 47 26 3 79 53 44 8 71 75 42 11 34 39 79 33 10 26 23 23 17 14 54 41 60 31 83 5 45 4 14 35 6 60 28 48 23 18 60 36 21 28 7 34 9 25 52 43 54 19".split()
w=set(r)
if len(w) < k:
    print("NO")
else:
    print ("YES")
    a=' '.join([str(r.index(e)+1) for e in list(w)[:k]])
    print(a)
