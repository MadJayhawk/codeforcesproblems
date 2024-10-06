#  https://codeforces.com/problemset/problem/489/B -  BerSU Ball

# Difficulty: 1300


def bersu_ball(b, boys, g, girls):
    d = []
    for i in girls:
        d.append([i - 1, i, i + 1])
    cnt = 0
    for i in boys:
        for j in range(g):
            if i in d[j]:
                cnt += 1
                d[j] = [0, 0, 0]
                break

    return cnt


if __name__ == "__main__":
    b = int(input())
    boys = sorted(list(map(int, input().split())))
    g = int(input())
    girls = sorted(list(map(int, input().split())))
    print(bersu_ball(b, boys, g, girls))

"""
I=lambda:sorted(map(int,input().split()))
n=I()[0]
a=I()
m=I()[0]
b=I()
i,j,k=0,0,0
while i<n and j<m:
	if abs(a[i]-b[j])<2:k+=1;i+=1;j+=1
	elif a[i]<b[j]:i+=1
	else:j+=1
print(k)
---------------------------------------------------------
n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
B = list(map(int, input().split()))
B.sort()
pairs = 0
while len(A) and len(B):
    if abs(A[0] - B[0]) <= 1:
        pairs += 1
        del A[0]
        del B[0]
    elif A[0] < B[0]:
        del A[0]
    else:
        del B[0]
print(pairs)
"""

"""
3
6 3 4
3
4 5 2
"""
