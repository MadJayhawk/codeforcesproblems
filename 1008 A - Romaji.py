# http://codeforces.com/contest/1008/problem/0  Romaji
s=input()
v= "aouie"
b=''
for i in s:
    if i in v:
        b+='0'
    elif i == 'n':
        b+='2'
    else:
        b+='1'
if '11' in b or '12' in b or s[-1] not in v+'n':
    print('NO')
else:
    print('YES')
--------------------------------------------------------------------------------------
Input
aucunuohja
Answer
NO
--------------------------------------------------------------------------------------
By liyd.sl2, contest: Codeforces Round #497 (Div. 2), problem: (A) Romaji, Accepted, #
 def isconsonant(x):
    return not x in "aeioun"

def isvowel(x):
    return x in "aeiou"

s = input()

s += "n"
flag = True
for i in range(0, len(s)-1):
    if isconsonant(s[i]) and not isvowel(s[i+1]):
        flag = False

if flag:
    print("YES")
else:
    print("NO")
--------------------------------------------------------------------------------------
By eugalt, contest: Codeforces Round #497 (Div. 2), problem: (A) Romaji, Accepted, #
 v='aouie'
s=input()+'b'
print(('NO','YES')[all(x in v+'n'or y in v for x,y in zip(s,s[1:]))])
--------------------------------------------------------------------------------------
By
junior08, contest: Codeforces
Round  # 497 (Div. 2), problem: (A) Romaji, Accepted, #
s=input( )
vowel='aeiou'
flag=0

if (s[-1] not in vowel) and s[-1]!='n':
    flag=1
##    print('a')

if s[0] in vowel:
    last='v'
elif s[0]=='n':
    last='n'
else:
    last='c'

for i in range(1, len(s)):
    if s[i] in vowel:
        last='v'
    elif (s[i] not in vowel and s[i]!='n') and (last=='v' or last=='n'):
        last='c'
    elif s[i]=='n' and last=='n' or last=='v':
        last='n'
    elif s[i]=='n' and last=='c':
        flag=1
        break
    else:
        ##        print(s[i], i)
        flag=1
        break
if flag:
    print('NO')
else:
    print('YES')
--------------------------------------------------------------------------------------
By codash, contest: Codeforces Round #497 (Div. 2), problem: (A) Romaji, Accepted, #
 s = (input().strip())
l = len(s)
ans = True
vowel = list('aeiou')
for i in range(l):
	if s[i] in vowel:
		continue
	else:
		if s[i] == 'n':
			continue
		else:
			if i + 1 == l:
				ans = False
				break
			else:
				if s[i + 1] not in vowel:
					ans = False
					break
if ans:
	print("YES")
else:
	print("NO")
