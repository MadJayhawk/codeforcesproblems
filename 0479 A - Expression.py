# https://codeforces.com/contest/xxxx/problem/x -  Expression
# Start:    Finish:     Duration:    Attempts:  1   Difficulty: 1100

def expression(e):
    a, b, c = e
    g = []
    g.append(a + b + c)
    g.append(a * b * c)
    g.append(a + b * c)
    g.append(a * b + c)
    g.append((a + b) * c)
    g.append(a + (b * c))
    g.append((a * b) + c)
    g.append(a * (b + c))
    return max(g)
# --------------------------------------------------------------
if __name__ == '__main__':
    d = []
    for i in range(3):
        d.append(int(input()))
    print(expression(d))

# --------------------------------------------------------------
a,b,c=[int(input())for i in'abc']
print(max(a*b*c,a*(b+c),(a+b)*c,a+b+c))