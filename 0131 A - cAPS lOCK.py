# https://codeforces.com/contest/xxxx/problem/x -  cAPS lOCK
# Start:    Finish:     Duration:    Attempts:  2   Difficulty: 1100

def caps_lock(s):
    b=s
    if s.islower() and len(s)==1:
        b=s.upper()
    if s.isupper():
        b=s.lower()
    if s[0].islower() and s[1:].isupper():
        b=s[0].upper()+s[1:].lower()
    return b
# --------------------------------------------------------------
if __name__ == '__main__':
    print(caps_lock(input()))
    # print(caps_lock('CAPS'))
    # print(caps_lock('cAPS'))
    # print(caps_lock('Lock'))
    # print(caps_lock('CaPs'))