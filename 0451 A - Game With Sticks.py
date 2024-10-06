# https://codeforces.com/contest/xxxx/problem/x -  Game With Sticks

def Game_With_Sticks (n, m):
    if min(n,m)%2 != 0:
        return "Akshat"
    else:
        return  "Malvika"
# --------------------------------------------------------------
if __name__ == '__main__':
    # n, m = list(map(int, input().split()))
    # print(Game_With_Sticks(n, m))

    b = '100 100'
    n, m = list(map(int, b.split()))
    print(Game_With_Sticks(n, m))

    b = '3 4'
    n, m = list(map(int, b.split()))
    print(Game_With_Sticks(n, m))

    b = '3 3'
    n, m = list(map(int, b.split()))
    print(Game_With_Sticks(n, m))

