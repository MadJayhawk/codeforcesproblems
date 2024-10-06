# https://codeforces.com/problemset/problem/469/A -   I Wanna Be The Guy
# Start:    Finish:     Duration:    Attempts:  1   Difficulty: 1000
 
def I_Wanna_Be_The_Guy(n,r,s):
    t = set(r+s)
    if len(t) ==  n:
        return "I become the guy."
    else:
        return "Oh, my keyboard!"
# --------------------------------------------------------------
if __name__ == '__main__':
    # n = int(input())
    # X = list(map(int, input().split()))[1:]
    # Y = list(map(int, input().split()))[1:]
    # print(I_Wanna_Be_The_Guy(n,X,Y))
    n = 4
    b = '3 1 2 3'
    c = "2 2 4"
    X = list(map(int, b.split()))[1:]
    Y = list(map(int, c.split()))[1:]
    print(I_Wanna_Be_The_Guy(n,X,Y))
    n = 4
    b = '3 1 2 3'
    c = "2 2 3"
    X = list(map(int, b.split()))[1:]
    Y = list(map(int, c.split()))[1:]
    print(I_Wanna_Be_The_Guy(n,X,Y))
