#https://codeforces.com/problemset/problem/580/A -  Kefa and First Steps
# Start: 9:13    Finish: xx    Duration: xx   Attempts: 2    Difficulty: 1000

def kefa_and_first_steps(n,a):
    cnt = 1
    k = 1
    c = a[0]
    for i in range(1, n):
        if a[i] >= a[i-1]:
            cnt += 1
            if cnt>k:
                k=cnt
        else:
            c=a[i]
            cnt=1
    return max(k,cnt)
# --------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(kefa_and_first_steps(n,a))
    # n = 6
    # b = '2 2 1 3 4 1'
    # a = list(map(int, b.split()))
    # print(kefa_and_first_steps(n,a))
    # n = 3
    # b = '2 2 9'
    # a = list(map(int, b.split()))
    # print(kefa_and_first_steps(n,a))