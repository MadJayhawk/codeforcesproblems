# https://codeforces.com/problemset/problem/519/A -  A and B and Chess
# Start:    Finish:     Duration:    Attempts:  1   Difficulty:  1100

def a_and_b_and_chess(a):
    t = [a[h] for h in range(len(a)) if a[h] != '.']
    pw = ['Q','R','B','N','P','K']
    pb = ['q','r','b','n','p','k']
    values =[9,5,3,3,1,0]
    w = dict(zip(pw,values))
    b = dict(zip(pb,values))
    w_sum = 0
    b_sum = 0
    for i in t:
        if i.isupper():
            w_sum += w[i]
        else:
            b_sum += b[i]
    if w_sum > b_sum:
        return "White"
    elif w_sum<b_sum:
        return "Black"
    else:
        return "Draw"


if __name__ == '__main__':
    s = ''
    for i in range(8):
        s += input()
    print(a_and_b_and_chess(s))

