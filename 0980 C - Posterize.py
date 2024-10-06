#http://codeforces.com/contest/980/problem/C
#n,k=map(int,input().split())
n=10
k=3
ar=[-1 for i in range(256)]

#ls=list(map(int,input().split()))
ls=[112, 184, 161, 156,118, 231, 191, 128 ,91, 229]
for e in ls:

    if ar[e]==-1:
        tmp=max(0,e-k+1)
        print(ar[e],tmp,e,e-k+1)
        for i in range(tmp,e+1):
            if ar[i]!=-1 and ar[i]!=i:
                tmp+=1
                continue
            else:
                while i<=e:
                    ar[i]=tmp
                    i+=1
    print("++",ar[e],end=" ")
-----------------------------------------------------------------

def main():
	n, k = [int(_) for _ in input().split()]
	a = [int(_) for _ in input().split()]

	p = [-1] * 256
	p[0] = 0

	for x in a:
		if p[x] < 0:
			for y in range(x - 1, max(-1, x - k), -1):
				if p[y] >= 0:
					if p[y] + k > x:
						p[x] = p[y]
					else:
						p[x] = p[y + 1] = y + 1

					break
			if p[x] < 0:
				p[x] = p[x - k + 1] = x - k + 1

	b = [p[x] for x in a]

	print(' '.join(map(str, b)))

if __name__ == '__main__':
	main()
    -----------------------------------------------------------------------------
N, K = input().split()
N, K = int(N), int(K)
P = [int(x) for x in input().split()]
A = [None]*256
A[0] = 0
for i in range(N):
    pn = P[i]
    if A[pn] is None:
        for j in range(K-1, -1, -1):
            if pn < j: continue
            if A[pn-j] is None:
                A[pn-j] = pn-j
                break
            else:
                if A[pn-j] + K - 1 >= pn:
                    break
        for jj in range(j, -1, -1):
            A[pn-jj] = A[pn-j]
print(*[A[P[i]] for i in range(N)])
