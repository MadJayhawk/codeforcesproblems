# https://codeforces.com/problemset/problem/1198/A -  MP3

# Difficulty:

from itertools import groupby


def mp3(n, I, a):
    k = int((I * 8) / n)
    d = 1 << k
    c = [len(list(group)) for (key, group) in groupby(sorted(a))]
    chgs = sum(c[d:])
    ans = chgs
    for i in range(0, len(c) - d):
        chgs += c[i]
        chgs -= c[i + d]
        ans = min(ans, chgs)
    return ans


if __name__ == "__main__":
    nn, II = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    print(mp3(nn, II, aa))
# 6 1
# 2 1 2 3 4 3
#
# 6 2
# 2 1 2 3 4 3
#
# 10 1
# 589934963 440265648 161048053 196789927 951616256 63404428 660569162 779938975 237139603 31052281
