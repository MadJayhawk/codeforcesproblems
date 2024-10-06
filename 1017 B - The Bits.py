# http://codeforces.com/contest/1017/problem/B  The Bits
n = int(input())
d = input()
e = input()
a = int(d,2)
b = int(e,2)
c = a | b
f = a ^ b
print(bin(a),bin(b), bin(c),bin(f))
print(d[2])


# # to convert A into B
#
# # Function that count set bits
# def countSetBits(n):
#     count = 0
#     while n:
#         count += n & 1
#         n >>= 1
#     return count
#
#
# # Function that return count of
# # flipped number
# def FlippedCount(a, b):
#     # Return count of set bits in
#     # a XOR b
#     return countSetBits(a ^ b)
#
#
# # Driver code
# a = 10
# b = 20
# print(FlippedCount(a, b))
