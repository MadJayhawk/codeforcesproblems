# https://codeforces.com/contest/230/problem/A -  Dragons
# def dragons_game(k, dd):
#     d = sorted(dd, key = lambda x: (x[0], x[1]))
#     for i in d:
#         if k <= i[0]:
#             return 'NO'
#         else:
#             k += i[1]
#     return 'YES'
#
#
# # --------------------------------------------------------------
# if __name__ == '__main__':
#     s, n = list(map(int, input().split()))
#     d = []
#     for i in range(n):
#         a, b = list(map(int, input().split()))
#         d.append([a, b])
#     print(dragons_game(s, d))
    # s = 2
    # n = 2
    # r = ['1 99','100 0']
    # d=[]
    # e=[]
    # for i in r:
    #     f,b=list(map(int, i.split()))
    #     d.append(f)
    #     e.append(b)
    # print(dragons(s, d,e))
    # s = 60
    # n = 3
    # r = ['90 5','20 15','10 10']
    # d=[]
    # e=[]
    # for i in r:
    #     f,b=list(map(int, i.split()))
    #     d.append(f)
    #     e.append(b)
    # print(dragons(s, d,e))
    # s = 10
    # n = 1
    # r = ['100 100']
    # d=[]
    # e=[]
    # for i in r:
    #     f,b=list(map(int, i.split()))
    #     d.append(f)
    #     e.append(b)
    # print(dragons(s, d,e))
# --------------------------------------------------------------
f = lambda: map(int, input().split())
s, n = f()
for a, b in sorted(list(f()) for i in ' ' * n):
    print(a,b,s)
    s = (s + b) * (s > a)
print('YNEOS'[s < 1::2])
