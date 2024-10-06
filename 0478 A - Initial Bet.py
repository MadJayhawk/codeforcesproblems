# https://codeforces.com/problemset/problem/478/A -  Initial Bet
# Start:    Finish:     Duration:    Attempts:  2   Difficulty: 1200

def initial_bet(n, b):
    d = sum([int(i) for i in b])
    if d%n == 0 and d != 0 :
        return d//n
    else:
        return -1


# --------------------------------------------------------------
if __name__ == '__main__':
    c = list(map(int, input().split()))
    print(initial_bet(len(c),c))
    
    # test_data = '2 5 4 0 4'
    # dt = list(map(int, test_data.split()))
    # print(initial_bet(5,dt))
    #
    # test_data = '4 5 9 2 1'
    # dt = list(map(int, test_data.split()))
    # print(initial_bet(5,dt))

