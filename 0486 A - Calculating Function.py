# https://codeforces.com/contest/xxxx/problem/x -  Calculating Function
# Start:    Finish:     Duration:    Attempts:     Difficulty: 

def calculating_function(a):
    if a % 2 != 0:
        ans = -1 * (a // 2 + 1)
    else:
        ans = a // 2
    return ans
# --------------------------------------------------------------
if __name__ == '__main__':
    print(calculating_function(int(input())))
    # print(calculating_function(4))
    # print(calculating_function(5))
    # print(calculating_function(10**15))