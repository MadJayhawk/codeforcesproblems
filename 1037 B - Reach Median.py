#https://codeforces.com/contest/1037/problem/B -  Reach Median

n,s = map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a)
m=n//2
ans=abs(a[m]-s)
ans+=sum(max(0,x-s)for x in a[:m])
ans+=sum(max(0,s-x)for x in a[m+1:])
print(ans)
#######################################################################
n,s=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
i=0
mid=n//2;
out=abs(li[mid]-s);
li[mid]=s;
# print(li)
while(i<mid):
    if li[i]>s:
        out +=abs(s-li[i])
    i+=1
i+=1
while(i<n):
    if(li[i]<s):
        out+=abs(s-li[i])
    i+=1
print(out
#############################################################################
def solve(s, arr):
    arr.sort()
    ans = 0
    i = len(arr) // 2
    if arr[i] < s:
        ans += s - arr[i]
        i += 1
        while i < len(arr) and arr[i] < s:
            ans += s - arr[i]
            i += 1
    else:
        ans += arr[i] - s
        i -= 1
        while i > -1 and arr[i] > s:
            ans += arr[i] - s
            i -= 1
     return ans;
# Main
def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(s, arr))
# end main

# Program Start
if __name__ == "__main__":
    main()
#######################################################################################
n,s=map(int, input().split())
ar=list(map(int, input().split()))
ar.sort()
z=(n//2)
q=0
if ar[z]<s:
    for i in range(z,n):
        if ar[i]<s:
            q+=s-ar[i]
        else:
            break
else:
    for i in range(z,-1,-1):
        if ar[i]>s:
            q+=ar[i]-s
        else:
            break
print(q)




    

