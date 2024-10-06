#http://codeforces.com/contest/1008/problem/C   Reorder the Array

DID NOT COMPLETE

n=int(input())
a=list(map(int,input().split()))
d = {}
for i in range(n):
    if a[i] in d.keys():
        d[a[i]] += 1
    else:
        d[a[i]] = 1
print(d)
m = d[a[i]]
print(m,i,a[i])
for elem in d.values():
    print (elem,m)
    if elem > m:
        m = elem
print(n-m)
-------------------------------------------------------------------------------
By reacheight, contest: Codeforces Round #497 (Div. 2), problem: (C) Reorder the Array, Accepted, #
 n = int(input())

d = {}
a = list(map(int, input().split()))
for x in a:
    if x in d.keys():
        d[x] += 1
    else:
        d[x] = 1

ans = 0
while True:
    c = 0
    for k, v in d.items():
        if v != 0:
            c += 1
            d[k] -= 1
    if c -1 <= 0:
        break
    ans += c - 1

print(ans)
-------------------------------------------------------------------------------
By k3hi, contest: Codeforces Round #497 (Div. 2), problem: (C) Reorder the Array, Accepted, #
 def main():
    t = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 0
    count = 0
    aux = t - a.count(a[0])
    for i in range(1,t):
        if a[i] != a[i-1]:
            aux = min(aux,t-i)
            ans+= min(aux,i-count)
            aux -= i-count
            count = i
            # print(aux,count,ans)
            if aux<=0:
                break
    print(ans)

if __name__ == '__main__':
    main()
-------------------------------------------------------------------------------
By NickyLogan, contest: Codeforces Round #497 (Div. 2), problem: (C) Reorder the Array, Accepted, #
 n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
ai, bi = 0, 0
c = 0
while bi < n and ai < n:
  if arr[bi] > arr[ai]:
    c += 1
    ai += 1
  bi += 1
print(c)
-------------------------------------------------------------------------------
By vyassamir1105, contest: Codeforces Round #497 (Div. 2), problem: (C) Reorder the Array, Accepted, #
 n = int(input())

nums = [int(i) for i in input().split()]

nums.sort()

i,j = 0,1
out = 0

while j < len(nums):
    if nums[j] > nums[i]:
        out += 1
        i += 1
        j += 1
    else:
        j += 1

print(out)
-------------------------------------------------------------------------------
By MIHAWK_HAWKEYE, contest: Codeforces Round #497 (Div. 2), problem: (C) Reorder the Array, Accepted, #
 n = int(input())
a = list(map(int, input().split()))

a.sort()

i=0
j=0
while i<n:
	if a[i]>a[j]:
		j+=1
	i+=1

print(j)
-------------------------------------------------------------------------------


