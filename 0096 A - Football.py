#  https://codeforces.com/problemset/problem/96/A-  Football
# Start:    Finish:     Duration:    Attempts:  1   Difficulty: 1100

def football(p):
    if '1111111' in p or '0000000' in p:
        return "YES"
    else:
        return "NO"
# --------------------------------------------------------------
if __name__ == '__main__':
    p = input()
    print(football(p))
    # print(football('001001'))
    # print(football('1000000001'))
# --------------------------------------------------------------
s = input()
if '0'*7 in s or '1'*7 in s:
    print('YES')
else:
    print('NO')
