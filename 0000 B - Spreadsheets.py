
#http://codeforces.com/contest/1/problem/B
# 4/6/18
import re
def RC(a):
	x=0
	for c in a:
		x=x*26+(ord(c)-ord('A')+1)
	return x
def notRC(b):
	x=''
	while b!=0:
		b-=1
		x=chr(b%26+ord('A'))+x
		b//=26
	return x
x="R5C6"  # or x="DWS456"

y=re.search('R([0-9]+)C([0-9]+)', x)

if y is not None:
		print('%s%s'%(notRC(int(y.group(2))),y.group(1)))
else:
	y=re.match('([A-Z]+)(\d+)',x)
	print('R%dC%d'%(int(y.group(2)),RC(y.group(1))))
