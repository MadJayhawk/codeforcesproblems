# https://codeforces.com/contest/579/problem/A -  Raising Bacteria
'''
Hint:
Write down x into its binary form. If the ith least significant bit is 1 and x contains n bits, we put one bacteria into this box in the morning of (n + 1 - i)th day. Then at the noon of the nth day, the box will contain x bacteria. So the answer is the number of ones in the binary form of x.
'''


def raising_bacteria(b):
   return str(bin(b)).count('1')
# --------------------------------------------------------------
if __name__ == '__main__':
    x = int(input())
    print(raising_bacteria(x))
    #
    # x = 536870911
    # print(raising_bacteria(x))
    # x = 5
    # print(raising_bacteria(x))
    # x = 8
    # print(raising_bacteria(x))

