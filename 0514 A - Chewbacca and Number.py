# https://codeforces.com/problemset/problem/514/A -  name of problem

# Difficulty: 1200


def chewbacca(nn):
    list1 = [int(i) for i in nn]
    list2 = [9 - i for i in list1]
    if list2[0] == 0:
        list2 = [9] + list2[1:]
    d = []
    for i in range(len(list1)):
        d.append(str(min(list1[i], list2[i])))

    x = "".join(d)

    return x


if __name__ == "__main__":
    n = input()
    print(chewbacca(n))
