#  https://codeforces.com/contest/1015/problem/C  Songs Compression
from itertools import permutations
def find_combination_equal_to_sum(lst,sum_of_combo):  #[497, 10, 5084, 156, 381, 3298, 625] , 781 ----> (156, 625)
    a=[]
    for i in range(1, len(lst) + 1):
        for combo in permutations(lst, i):
            if sum(combo) == sum_of_combo:
               a.append(len(combo))
    return a

M = lambda: list(map(int,input().split()))
n, m = M()
s=[]
for i in range(n):
    a,b = M()
    s.append(a-b)
ss=sum(s)
w=ss-m
print(w)
t=0
d=list(find_combination_equal_to_sum(s , w))
e=set(d)
print(*e)