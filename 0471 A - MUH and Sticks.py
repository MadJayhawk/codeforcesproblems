# https://codeforces.com/problemset/problem/471/A -  MUH and Sticks

# Difficulty: 1200


def muh_and_sticks(values):
    a = list(
        map(
            lambda val: (val, len([i for i in range(len(values)) if values[i] == val])),
            values,
        )
    )
    b = list(set(list(zip(*a))[1]))
    if b == [6] or b == [2, 4]:
        return "Elephant"
    elif b == [1, 5] or b == [1, 4]:
        return "Bear"
    else:
        return "Alien"


if __name__ == "__main__":
    a = list(map(int, input().split()))
    print(muh_and_sticks(a))
