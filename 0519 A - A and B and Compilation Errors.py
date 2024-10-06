# https://codeforces.com/problemset/problem/519/B -  A and B and Compilation Errors
# Start:    Finish:     Duration:    Attempts:  5   Difficulty: 1200

def compilation_errors(r):
    for i in range(0,len(r)-1):
        print(sum(r[i]) - sum(r[i+1]))

if __name__ == '__main__':
    n = int(input())
    d = []
    d.append(list(map(int, input().split())))
    d.append(list(map(int, input().split())))
    d.append(list(map(int, input().split())))
    compilation_errors(d)
#------------------------------------------------------------------------------------
# import operator
# from functools import reduce
# n=input()
# a=[0]*3
# for i in[0,1,2]:
#  a[i]=reduce(operator.xor,map(int,input().split()))
# print(a[0]^a[1])
# print(a[1]^a[2])
