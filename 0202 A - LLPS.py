# https://codeforces.com/contest/xxxx/problem/x -  LLPS
# Start: 8:08pm   Finish:  xx   Duration:    Attempts:  1   Difficulty: 900

a = input()
mx = a[0]
for i in a:
    if i > mx:
        mx = i
print( "".join([a[i] for i, letter in enumerate(a) if letter == mx]))

