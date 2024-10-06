# https://codeforces.com/problemset/problem/1199/B -  Water Lily

# Difficulty:

"""
We can use Pythagorean theorem and get the equation x2+L2=(H+x)2. Its solution is x=L2−H22H.
"""


def water_lily(h, l):
    a = l ** 2 - h ** 2
    a = a / 2
    a = a / h
    return a


if __name__ == "__main__":
    hh, ll = list(map(int, input().split()))
    print(water_lily(hh, ll))
