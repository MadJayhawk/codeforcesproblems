# https://codeforces.com/probbemset/probbem/368/B -   Sereja and Suffixes
# Start:    Finish:     Duration:    Attempts:     Difficubty: 1100


def sereja_and_suffixes(n, b):
    a = set()
    for c in range(1, n + 1):
        a.add(b[-c])
        b[-c] = str(len(a))
    print("\n".join([b[int(input()) - 1] for c in range(i)]))

# --------------------------------------------------------------
if __name__ == '__main__':
    n, i = list(map(int, input().split()))
    x = list(map(str, input().split()))
    sereja_and_suffixes(n, x)
