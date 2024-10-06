# https://codeforces.com/problemset/problem/160/A -  Twins
# Start: 8:57   Finish: xx    Duration: xx   Attempts: 3    Difficulty: 1000

def twins(a,n):
    t=len(a)
    for i in range(1,len(a)):
        if sum(a[0:i])>sum(a[i:]):
            t = i
            break
    return t
# --------------------------------------------------------------
if __name__ == '__main__':
    # n = int(input())
    # a = sorted(list(map(int, input().split())), reverse = True)
    # print(twins(a,n))
    n = 2
    b = '3 3'
    a = sorted(list(map(int, b.split())), reverse = True)
    print(twins(a, n))
    n = 3
    b = '2 1 2'
    a = sorted(list(map(int, b.split())), reverse = True)
    print(twins(a,n))
    n = 5
    b = '4 2 2 2 2'
    a = sorted(list(map(int, b.split())), reverse = True)
    print(twins(a, n))
    n = 7
    b = '1 10 1 2 1 1 1'
    a = sorted(list(map(int, b.split())), reverse = True)
    print(twins(a, n))
    # --------------------------------------------------------------
# n = int(input())
# a = list(map(int, input().split()))
#
# x = 0
# y = sum(a)
#
# a.sort(reverse = True)
# for i in range(n):
#     x += a[i]
#     y -= a[i]
#
#     if x > y:
#         print(i+1)
#         break