# https://codeforces.com/1133/problem/A -  Middle of the Contest
def middle_of_the_contest(times):
    a = []
    for i in range(0,2):
        h, m = map(int,times[i].split(":"))
        a.append([h,m,h*60+m])
    b = a[0][2]+(a[1][2]-a[0][2])//2
    return f'{b//60:0>2}:{b%60:0>2}'
t = input()
s = input()
print(middle_of_the_contest([t,s]))



