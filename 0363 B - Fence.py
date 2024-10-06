# https://codeforces.com/problemset/problem/363/B-  Fence
# Start:    Finish:     Duration:    Attempts:     Difficulty: 1200

n, k = list(map(int, input().split()))
h = list(map(int, input().split()))
a = [0] * (n - k + 1)
a[0] = sum(h[0:k])
for i in range(1, n - k + 1):
    a[i] = a[i - 1] + h[i + k - 1] - h[i - 1]
print(a.index(min(a)) + 1)
