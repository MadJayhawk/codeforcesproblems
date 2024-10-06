# https://codeforces.com/problemset/problem/149/A -   Business Trip
# Start:    Finish:     Duration:    Attempts:  2   Difficulty: 1100

def business_trip(n, a):
    if n == 0:
        return 0
    c = 0
    for cnt, i in enumerate(a,start=1):
        c += i
        if c >= n:
            return cnt
    return -1

if __name__ == '__main__':
    k = int(input())
    a = sorted(list(map(int, input().split())), reverse = True)
    print(business_trip(k, a))
    #
    # k = 5
    # a = sorted(list(map(int, '1 1 1 1 2 2 3 2 2 1 1 1'.split())),reverse=True)
    # print(business_trip(k,a))
    # k = 0
    # a = sorted(list(map(int, '0 0 0 0 0 0 0 1 1 2 3 0'.split())),reverse=True)
    # print(business_trip(k,a))
    # k = 11
    # a = sorted(list(map(int, '1 1 4 1 1 5 1 1 4 1 1 1'.split())),reverse=True)
    # print(business_trip(k,a))