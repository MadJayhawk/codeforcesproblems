# https://codeforces.com/problemset/problem/439/A -  Devu, the Singer and Churu, the Joker
# Start:    Finish:     Duration:    Attempts: 3    Difficulty:1100

def singer_and_joker(nn,mm,tt):
    s = sum(tt)+(nn-1)*10
    if s <= mm:
         return (mm-s)//5+((nn-1)*2)
    else:
        return -1


if __name__ == '__main__':
    f = lambda: map(int, input().split())
    n, m = f()
    t = list(f())
    print(singer_and_joker(n, m, t))
#     n,m = map(int, ('1 30').split())
#     t = map(int, ('').split())
#     print(singer_and_joker(n,m,t))
#     n, m = map(int, ('7 100').split())
#     t = map(int, ('2 1 1 5 6 6 3').split())
#     print(singer_and_joker(n,m,t))