# https://https://codeforces.com/problemset/problem/734/A -  Anton and Danik
# Start: 7:41pm     Finish: 7:56    Duration:  15 minutes  1 attempt     Rating:  700

n = int(input())
v = input()
if v.count('A')>v.count('D'):
    print('Anton')
elif v.count('D')>v.count('A'):
    print('Danik')
else:
    print('Friendship')

