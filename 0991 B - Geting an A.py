#http://codeforces.com/contest/991/problem/B
n= int(input())
#n=6
g=sorted(list(map(int,input().split())))
s=sum(g)
a=round(s/n+.05)
cnt=0
if a==5:
    print (cnt)
else:
    for i in g:
        s=s-i+5
        a=round(s/n+.05)
        cnt+=1
        # print (i,s,a,cnt)
        if a==5:
            print (cnt)
            break
------------------------------------------------------------------------------------
SOLUTIONS
10
2 4 5 5 5 5 2 3 3 2
Answer
3

------------------------------------------------------------------------------------
By lucas.vieira, contest: Codeforces Round #491 (Div. 2), problem: (B) Getting an A, Accepted, #
 n = int(input())
numbers = sorted(list(map(int, input().split(' '))))

redo = 0

def average():
    return sum(numbers) / n

while (average() < 4.5):
    redo += 1
    if numbers[redo - 1] < 5:
        numbers[redo - 1] = 5

print(redo)
-------------------------------------------------------------------------------------------
MIS = lambda: map(int,input().split())
n = int(input())
L = sorted(MIS())

for i in range(n):
    if sum(L)*2 >= 9*n:
        print(i)
        break
    L[i] = 5
else: print(n)
----------------------------------------------------------------------------------------------
n = int(input())

grades = [int(x) * 2 for x in input().split()]

res = sum(grades)
target = 9 * len(grades)

grades.sort()

for i, grade in enumerate(grades):
    if res >= target:
        print(i)
        break
    else:
        res += 10 - grade
else:
    print(len(grades))
-------------------------------------------------------------------------------------------
By _Kee, contest: Codeforces Round #491 (Div. 2), problem: (B) Getting an A, Accepted, #
 #!/usr/bin/python3

def solve(N, A):
    thre = N * 4 + N // 2
    if N % 2 > 0:
        thre += 1

    A.sort()

    s = sum(A)

    c = 0
    while s < thre:
        s += 5 - A[c]
        c += 1

    return c


def main():
    N = int(input())
    A = [int(e) for e in input().split(' ')]
    assert len(A) == N
    print(solve(N, A))


if __name__ == '__main__':
    main()
--------------------------------------------------------------------------------------------------
By ipeisbouri64, contest: Codeforces Round #491 (Div. 2), problem: (B) Getting an A, Accepted, #
 n=int(input())
t=list(map(int,input().split()))
k=0
for i in range(n):
    k+=t[i]
    t[i]=t[i]-5
t.sort()
h=4.5*n
i=0
while k<h:
    k-=t[i]
    i+=1
    if i==n:
        break
print(i)
---------------------------------------------------------------------------------------------------
n = int(input())
a = list(map(int,input().split()))
a.sort()
i = 0
ari = sum(a)/len(a)
if ari>=4.5:
    print(0)
else:
    while ari<4.5:
        a[i]=5
        ari= sum(a)/len(a)
        i+=1
    print(i)
