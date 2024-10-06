# https://codeforces.com/contest/1185/problem/0 -  Ropewalkers
# Start:    Finish:     Duration:    Attempts:     Difficulty:

#import logging
# logging.basicConfig(format='%(message)s')
# logging.error(f'n: {n}')

def ropewalkers(w):
    d = w[3]
    u=sorted(w[0:3])
    s = u[1] - d
    t = d + u[1]
    if t < u[2]:
        t = 0
    else:
        t = t-u[2]
    if u[0] <= s:
        s=0
    else:
        s = d-u[1]+u[0]
    return abs(s+t)

if __name__ == '__main__':
    aa= list(map(int, input().split()))
    print(ropewalkers(aa))


    # print(name_of_problem())

