# https://codeforces.com/problemset/problem/379/A -  New Year Candles
# Start:    Finish:     Duration:    Attempts:     Difficulty: 1100

def new_year_candles(c, d):
    x = c
    while c >= d:
        x += (c // d)
        c = (c// d) + (c % d)
    return x
# --------------------------------------------------------------
if __name__ == '__main__':
    f = lambda: map(int, input().split())
    a, b = f()
    print(new_year_candles(a,b))
    # a = 4
    # b =2
    # print('eee',new_year_candles(a,b))
