# https://codeforces.com/problemset/problem/270/A -  Fancy Fence
# Start:    Finish:     Duration:    Attempts: 1    Difficulty: 1200

def fancy_fence(a):
    if 360 %(180-a) == 0:
        return 'YES'
    else:
        return "NO"

# --------------------------------------------------------------
if __name__ == '__main__':
    t = int(input())
    b = [int(input()) for i in range(t)]
    for i in b:
        print(fancy_fence(i))


