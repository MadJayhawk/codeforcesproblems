# https://codeforces.com/problemset/problem/476/A -  Dreamoon and Stairs
# Start:    Finish:     Duration:    Attempts:  3   Difficulty: 1100

#import logging
# logging.basicConfig(format='%(message)s')
# logging.error(f'n: {n}')

def dreamoon_and_stairs(n, m):
    k = n // 2
    d = []
    for i in range(0, k+1):
        if (n-i)%m==0:
            d.append(n-i)
    if len (d)<= 0:
        return -1
    else:
        return min(d)
# --------------------------------------------------------------
if __name__ == '__main__':
    f = lambda: map(int, input().split())
    s,t = f()
    print(dreamoon_and_stairs(s,t))
    

    # s,t = [10,2]
    # print(dreamoon_and_stairs(s,t))
    # s,t = [3,5]
    # print(dreamoon_and_stairs(s,t))
