# https://codeforces.com/contest/xxxx/problem/x -  Little Elephant and Bits

# Difficulty:  1200


def little_elephant_and_bits(a):
    if "0" not in a:
        a.pop(a.index("1"))
    else:
        a.pop(a.index("0"))
    return "".join(a)


if __name__ == "__main__":
    a = list(input())
    print(little_elephant_and_bits(a))
