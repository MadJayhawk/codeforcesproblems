#  http://codeforces.com/contest/988/problem/B
n=int(input())
h=[]
for i in range(n):
    h.append(input())
h.sort(key = lambda s: len(s))
ans="YES"
for i in range(0,n-1):
    if h[i] not in h[i+1]:
        ans="NO"
print (ans)
for i in range(5):
    if ans is "YES":
        for e in h:
            print (e)
for i in h:


# def list_to_dict(lst):
#     knt=0
#     for i in lst:
#         s[i]=knt
#         knt+=1
#     return s
# def find(s, ss): # s= string ss=substring
#     return s.find(ss) != -1
# def in_string(s,ss):
#     return ss in s
# def index(s, ss):# s= string ss=substring
#     try:
#         s.index(ss)
#     except ValueError:
#         return False
#     else:
#         return True
#
# def sort_by_length(lst):  #sorts list members by length of the members
#     lst.sort(key = lambda s: len(s))
#     return lst
