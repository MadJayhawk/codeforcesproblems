#http://codeforces.com/contest/1011/problem/0   Stages

M = lambda: list(map(int,input().split()))
n, k = M()
# s = sorted(input())
t=[]
for code in map(ord, sorted(input())):
    t.append(code-96)
h=0
sm=0
cnt=0
j=sorted(set(t))
for i in j:
    if i!=h:
        sm+=i
        cnt+=1
        h=i+1
        if cnt==k:
            break
if cnt>=k:
    print(sm)
else:
    print(-1)
#---------------------------------------------------------------------------------------
By
Sanskar123, contest: Codeforces
Round  # 499 (Div. 2), problem: (A) Stages, Accepted, #
l = "abcdefghijklmnopqrstuvwxyz"

dicti = {}
for g in range(0, 26):
    dicti[l[g]] = g + 1

n, k = map(int, input().split())
string = input()

l1 = []
for val in range(len(string)):
    l1.append(string[val])
l1.sort()
sump = dicti[l1[0]]
t = 0
w = 1
s = 1
gk = 0
if (k == 1):
    print(sump)
else:

    while (s < len(l1) and gk < len(l1)):

        if (dicti[l1[s]] - dicti[l1[gk]] >= 2):
            w += 1
            gk = s
            s += 1
            sump += dicti[l1[s - 1]]
            if (w == k):
                t = 1
                break
        else:
            if (w == k):
                t = 1
                break
            else:
                s += 1
    if (t == 1):
        print(sump)
    else:
        print(-1)
---------------------------------------------------------------------------------------
By Rs15z, contest: Codeforces Round #499 (Div. 2), problem: (A) Stages, Accepted, #
 n, k = map(int, input().split())
s = input()
d = [False] * 26
for c in s:
    d[ord(c) - ord('a')] = True
w = 0
l = 0
i = 0
while (i < 26) and (l < k):
    if d[i]:
        w += i + 1
        l += 1
        i += 2
    else:
        i += 1
if (l == k):
    print(w)
else:
    print(-1)
---------------------------------------------------------------------------------------
By peterandluc, contest: Codeforces Round #499 (Div. 2), problem: (A) Stages, Accepted, #
 n, k = map(int, input().split())
a = sorted(list(set(input())))
cnt = 0
m = 0
flag = True
for i in range(len(a)):
    if cnt == k:
        break
    if i - 1 >= 0 and flag:
        if a[i-1] == chr(ord(a[i])-1):
            flag = False
            continue
    m += ord(a[i]) - ord('a') + 1
    cnt += 1
    flag = True
if cnt < k:
    print(-1)
else:
    print(m)
---------------------------------------------------------------------------------------
By zootyducky, contest: Codeforces Round #499 (Div. 2), problem: (A) Stages, Accepted, #
 input_list = list(map(int, input().split()))
input_alpha = list(input())

total_stage = input_list[0]
select_stage = input_list[1]
num_alpha = list(map(ord, input_alpha))
num_alpha_sorted= sorted(num_alpha)

ans_list = []
cur_min_weight = 0

for i in num_alpha_sorted:
    if len(ans_list) == select_stage:
        break;
    if cur_min_weight + 2 <= i:
        ans_list.append(i)
        cur_min_weight = i

if len(ans_list) < select_stage:
    print(-1)
else:
    sum_list = 0
    for j in ans_list:
        sum_list = sum_list + j - 96
    print(sum_list)
---------------------------------------------------------------------------------------
By eugalt, contest: Codeforces Round #499 (Div. 2), problem: (A) Stages, Accepted, #
n,k=map(int,input().split())
w=p=0
for c in map(ord,sorted((input()))):
 if c-p>1:
     w+=c-96
     p=c
     k-=1
 if k==0:break
print((w,-1)[k>0])
