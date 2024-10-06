# https://codeforces.com/problemset/problem/556/A  -  Case of the Zeros and Ones
# Start:    Finish:     Duration:    Attempts:  5   Difficulty: 1100

def case_of_the_zeros_and_ones(n, a):
     return abs(a.count('1')-a.count('0'))
# --------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    s = input()
    print(case_of_the_zeros_and_ones(n,s))
    
    # n = 8
    # s = list('11101111')
    # print(case_of_the_zeros_and_ones(n,s))
    # n = 1
    # s = '1'
    # print(case_of_the_zeros_and_ones(n,s))
    # n = 2
    # s = '00'
    # print(case_of_the_zeros_and_ones(n,s))
    # n = 2
    # s = '01'
    # print(case_of_the_zeros_and_ones(n, s))
