# https://codeforces.com/problemset/problem/48/A -  Rock-paper-scissors
# Start:10:43pm    Finish:     Duration: 1+ hour   Attempts: 1    Difficulty: 900

b = []
for i in range(3):
    b.append(input())
players =['F','M','S']
if 'paper' in b and b.count('rock')==2:
    print(players[(b.index('paper'))])
elif 'rock' in b and b.count('scissors')==2:
    print(players[(b.index('rock'))])
elif 'scissors' in b and b.count('paper')==2:
    print(players[(b.index('scissors'))])
else:
    print('?')
-----------------------------------------------------------------------
F=input()
M=input()
S=input()

Beater={"rock":"paper","paper":"scissors","scissors":"rock"}

if(F==M and S==Beater[F]):
    print("S")
elif(F==S and M==Beater[F]):
    print("M")
elif(S==M and F==Beater[S]):
    print("F")
else:
    print("?")
-----------------------------------------------------------------------
n, v = ['F', 'M', 'S'], [['rock', 'paper', 'scissors'].index(input()) for i in range(3)]
for i in range(3):
    if v[(i - 1) % 3] == (v[i] - 1) % 3 and v[(i + 1) % 3] == (v[i] - 1) % 3:
        print(n[i])
        exit()
print('?')