# http://codeforces.com/contest/980/problem/A
s="---------------------------------o----------------------------oo------------------------------------" #input()
ans="YES"
a = s.count('o')
b = s.count('-')
if  a and b % a :
    ans="NO"
print (ans)
# # print("NO" if a and b % a else "YES")
# a = s.count('o')
# b = s.count('-')
# print("NO" if a and b % a else "YES")
