# https://codeforces.com/problemset/problem/1075/A -  The Kings Race
# Start: 7:29   Finish: 7:44    Duration:  15  Attempts:  1   Difficulty: 900

n = int(input())
x,y = list(map(int, input().split()))
wx, wy = [1, 1]
bx, by =[n, n]
if x-wx+y-wy<=bx-x+by-y:
    print("White")
else:
    print("Black")
