#https://codeforces.com/contest/1029/problem/0 Many Equal Substrings
n,m=map(int,input().split())
s=input()
x=0
for i in range(1,n):
    if s[i::]==s[0:n-i]:
        x=n-i
        break
ans=s+s[x::]*(m-1)
print(ans)


#
# def get_test_data():
#     global n, m, s, t
#     t = ['3 4','3 2','1 50','25 24','4 25','8 4']
#     s = ['aba','cat','q','kyzdckyzdckyzdckyzdckyzdc','lclc','cababbcc']
#     n = [len(x) for x in t]
#     m = len(s)
#
# def get_problem_data():
#     global n, s
#     M = lambda: list(map(int, input().split()))
#     n, m = M()
#     s = input()
#
# def solve(m, s):
#     #put get_problem_data here
#     i = 1
#     while s[:-i] != s[i:]:
#         i += 1
#     print(s[:i] * m + s[i:])
#
# get_test_data()
# for j in range(0,len(s)):
#     e=list(map(int, t[j].split()))
#     solve(e[1], s[j])
#
# # get_problem_data()
# # print(['NO', 'YES'][solve(n, m, s, t)])
# ---------------------------------------------------------------------------------------------
# By d_a_r_k, contest: Codeforces Round #506 (Div. 3), problem: (A) Many Equal Substrings, Accepted, #
#  n,m=map(int,input().split())
# s=input()
# x=0
# for i in range(1,n):
#     if s[i::]==s[0:n-i]:
#         x=n-i
#         break
# ans=s+s[x::]*(m-1)
# print(ans)
# # ---------------------------------------------------------------------------------------------
# # By lifefeeder, contest: Codeforces Round #506 (Div. 3), problem: (A) Many Equal Substrings, Accepted, #
# #  def main(n, k, t):
# #     for i in range(1, n + 1):
# #         if t[i:] == t[:n - i]:
# #             s = t[:i]*k
# #             s += t[i:]
# #             print(s)
# #             break
# # n, k = map(int, input().split())
# # t = input()
# # main(n, k, t)
# # ---------------------------------------------------------------------------------------------
# # By guaNa, contest: Codeforces Round #506 (Div. 3), problem: (A) Many Equal Substrings, Accepted, #
# #  n,k=map(int,input().split())
# # s,s1=input(),''
# # c=1
# # min=99999
# # d=set(s)
# # if len(d)==1:
# #     print(s+s[0]*(k-1))
# #     exit()
# # while (c<len(s)):
# #     if s[:c]==s[len(s)-c:]:
# #         if min>len(s[:c]+s[c:]*k):
# #             min=len(s[:c]+s[c:]*k)
# #             s1=(s[:c]+s[c:]*k)
# #     c+=1
# # if s1!='':
# #     print(s1)
# # else:
# #     print(s*k)
# # ---------------------------------------------------------------------------------------------
# # By Tiko.T, contest: Codeforces Round #506 (Div. 3), problem: (A) Many Equal Substrings, Accepted, #
# #  # -*- coding: utf-8 -*-
# # n, k = map(int, input().split())
# # t = input()
# # i = 1
# # while i < n and t[i:] != t[:-i] : i += 1
# # print(t[:i] * k + t[i:])
# # ---------------------------------------------------------------------------------------------
# # By shado_w, contest: Codeforces Round #506 (Div. 3), problem: (A) Many Equal Substrings, Accepted, #
# #  n,m=map(int,input().strip().split())
# # r=input()
# # ans=""
# # ans1=""
# # for i in range(n-1):
# #     if r[:i+1]==r[n-1-i:]:
# #         ans=r[:i+1]
# # j=len(ans)
# # ans1=r+(m-1)*r[j:]
# # print(ans1)
# # ---------------------------------------------------------------------------------------------
# # By raphael99, contest: Codeforces Round #506 (Div. 3), problem: (A) Many Equal Substrings, Accepted, #
# #  n,k= map(int, input().split())
# # s=input()
# # l=0
# # print(s,end="")
# # for i in range(1,n):
# #     if s[i:] == s[0: n-i ]:
# #         l=len(s[i:])
# #         break
# #
# # print(s[l:]*(k-1))
# ---------------------------------------------------------------------------------------------