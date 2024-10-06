# https://codeforces.com/problemset/problem/118/A -  String Task
# Start:    Finish:     Duration:    Attempts:  1   Difficulty: 1100
def string_task(a):
    d = []
    for i in a:
        if i not in 'aeiouy':
            d.append('.'+i)
    return ''.join(d)
# --------------------------------------------------------------
if __name__ == '__main__':
    print(string_task(input().lower()))
    # s = 'tour'
    # print(string_task(s))
    # s = 'Codeforces'
    # print(string_task(s))
    # s = 'aBAcAba'
    # print(string_task(s))
