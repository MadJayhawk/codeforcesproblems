# https://codeforces.com/problemset/problem/584/A -  Olesya and Rodion
# Start:    Finish:     Duration:    Attempts:   1  Difficulty:  1100

def olesya_and_rodion(n, t):
    for i in range(10**(n-1),10**n):
        if i%t==0:
            return i
    return -1
# --------------------------------------------------------------
if __name__ == '__main__':
    f = lambda: map(int, input().split())
    n,t = f()
    print(olesya_and_rodion(n,t))

    
    # r,s = [5,11]
    # print(olesya_and_rodion(r,s))