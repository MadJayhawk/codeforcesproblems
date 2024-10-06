#http://codeforces.com/contest/982/problem/A - Row
n= int(input())
c= input()
# n=1
# c="1"
ans="Yes"
if "11" in c:
    ans="No"
else:
    if "000" in c:
        ans="No"
    else:
        if c.endswith('00') or c.startswith('00'):
            ans="No"
        else:
            if c=="0":
                ans="No"
print (ans)
