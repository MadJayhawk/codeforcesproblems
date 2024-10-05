# https://codeforces.com/contest/xxxx/problem/x -  Chat room
# Start:    Finish:     Duration:    Attempts:     Difficulty: 
import itertools
def chat_room(t):
    ans = 'NO'
    s = list(filter(lambda a: a in 'hello', t))
    for c in itertools.combinations(s, 5):
        if ''.join(c) == 'hello':
            ans = 'YES'
            break
    return ans
# --------------------------------------------------------------
if __name__ == '__main__':
    print(chat_room(input()))
    # print(chat_room('ahhellllloou'))
    # print(chat_room('hlelo'))
# --------------------------------------------------------------

s=iter(input());
print('NYOE S'[all(c in s for c in 'hello')::2])
# --------------------------------------------------------------
import re
print("YES" if re.search("h.*e.*l.*l.*o",input())else"NO")
# --------------------------------------------------------------
s=input()
l=['h','e','l','l','o']
t=''
i=0
for x in s:
    if i<5 and x==l[i]:
        t+=x
        i+=1
if t=="hello":
    print("YES")
else:
    print("NO")