#https://codeforces.com/problemset/problem/992/A  Nasty and an Array  passed at 1:56:22
# from collections import Counter
# n=int(input())
# a=list(map(int,input().split()))
# x=Counter(a)
# print (len(x)-x[0])
# ---------------------------------------
# SOLUTIONS
# 8
# -26 0 -249 -289 -126 -206 288 -11
# Answer
# 7
# ---------------------------------------
input()
print(set('-2075 -32242 27034 -37618 -96962 82203 64846 48249 -71761 28908 -21222 -61370 46899'.split()),len(set('-2075 -32242 27034 -37618 -96962 82203 64846 48249 -71761 28908 -21222 -61370 46899'.split()) - {'0'}))
# ---------------------------------------
# input()
# print(len(set(input().split()+["0"]))-1)
# ---------------------------------------
# input()
# print(len(set(filter(None,map(int,input().split())))))
# ---------------------------------------
# input()
# a = set(input().split())
# print(len(a) - (1 if '0' in a else 0))
# ---------------------------------------
# input()
# s = set(input().split())
# if '0' in s:
#     print(len(s) - 1)
# else:
#     print(len(s))
