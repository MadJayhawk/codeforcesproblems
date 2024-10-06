# https://codeforces.com/contest/69/problem/A -  Young Physicist
# Start:    Finish:     Duration:    Attempts:     Difficulty: 1100

def young_physicist(a):
    e=[]
    d = list(zip(*a))
    ans="YES"
    for i in d:
        if sum(i)!=0:
            ans = "NO"
    return ans
# --------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    d = []
    for i in range(n):
        f = lambda: map(int, input().split())
        x, y, z = f()
        d.append([x,y,z])
    print(young_physicist(d))
#     n = 3
#     d = []
#     b = ['4 1 7','-2 4 -1','1 -5 -3']
#     for i in range(n):
#         f = lambda: map(int, b[i].split())
#         x, y, z = f()
#         d.append([x,y,z])
#     print(young_physicist(d))
#
#     n = 3
#     d = []
#     b = ['3 -1 7', '-5 2 -4', '2 -1 -3']
#     for i in range(n):
#         f = lambda: map(int, b[i].split())
#         x, y, z = f()
#         d.append([x, y, z])
#     print(young_physicist(d))