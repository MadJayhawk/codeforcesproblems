# https://codeforces.com/contest/1025/problem/x -  Weakened Common Divisor
import itertools
def get_test_data():
    global n, m, s, t
    
    s = [['17 18','15 24','12 15'],['10 16','7 17'],['90 108','45 105' '75 40','165 175','33 30']]
    n = [len(x) for x in s]
    m = len(s)


def get_problem_data():
    global n, m, s, t
    M = lambda: list(map(int, input().split()))
    n, m = M()
    m = input()
    s=[]
    for i in range(m):
        s.append(M())

def greatest_common_denominator(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def solve(s):
    d=[]
    hld=0
    for i in range(len(s)):
        a,b=list(map(int, s[i].split()))
        d.append([a,b])
    print(d)
    for i in range(0,len(d)):
        for k in range(i,len(d)):
            xx = list(itertools.product(d[i], d[k]))
            print(xx)
            for j in xx:
                r = j[0]
                for h in j[1:]:
                    r = greatest_common_denominator(r, h)
                    if r>hld:
                        hld=r
                print(hld)



get_test_data()
for j in range(0, m):
    
    print(['NO', 'YES'][solve(s[j])])

# get_problem_data()
# print(['NO', 'YES'][solve(n, m, s, t)])