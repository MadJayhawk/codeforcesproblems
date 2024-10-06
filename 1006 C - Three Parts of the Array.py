#http://codeforces.com/contest/1006/problem/C   Three Parts of the Array

def three_parts_of_the_array(x):
    l = 0
    r = len(x) - 1
    r_sum = x[r]
    l_sum = x[l]
    maxx = 0
    while l < r:
        if l_sum > r_sum:
            r -= 1
            r_sum += x[r]
        elif r_sum > l_sum:
            l += 1
            l_sum += x[l]
        else:
            maxx = max([r_sum, maxx])
            r -= 1
            r_sum += x[r]
    return maxx

if __name__ == '__main__':
    n = int(input())
    R = lambda: list(map(int, input().split()))
    c = R()
    print(three_parts_of_the_array(c))

