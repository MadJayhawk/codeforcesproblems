--------------------------------------------------------------------------
http://codeforces.com/contest/994/problem/C
Input
-5 -5 5 -5 5 5 -5 5
6 0 0 6 -6 0 0 -6
Answer
YES
Input
-5 -5 5 -5 5 5 -5 5
-5 12 0 7 5 12 0 17
Answer
NO

--------------------------------------------------------------------------
By pyrus, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (C) Two Squares, Accepted, #

from sys import exit

q1 = list(map(int, input().strip().split()))
q2 = list(map(int, input().strip().split()))

xl = min(q1[::2])
xr = max(q1[::2])
yl = min(q1[1::2])
yr = max(q1[1::2])

xc = sum(q2[::2]) // 4
yc = sum(q2[1::2]) // 4

r = max(list(map(lambda x: x - xc, q2[::2])))

for i in range(4):
	x, y = q2[2*i: 2*i + 2]
	if xl <= x <= xr and yl <= y <= yr:
		print ('YES')
		exit()

for i in range(4):
	x, y = q1[2*i: 2*i + 2]
	if abs(x - xc) + abs(y - yc) <= r:
		print ('YES')
		exit()

if (xl + xr - 2 * xc)**2 + (yl + yr - 2 * yc)**2 <= 2 * r**2:
	print ('YES')
else:
	print ('NO')
--------------------------------------------------------------------------
By flygrounder, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (C) Two Squares, Accepted, #
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{} {}".format(self.x, self.y)


class Vector:
    @property
    def squared_length(self):
        return self.x**2 + self.y**2

    def __init__(self, p1, p2):
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y

    def __str__(self):
        return "{} {}".format(self.x, self.y)


def vector_multiply(v1, v2):
    return v1.x * v2.y - v1.y * v2.x


def scalar_multiply(v1, v2):
    return v1.x * v2.x + v1.y * v2.y


def check_angle(p, p1, p2, p3):
    v1 = Vector(p2, p1)
    v2 = Vector(p2, p)
    v3 = Vector(p2, p3)
    if (scalar_multiply(v1, v2) < 0) and (scalar_multiply(v1, v2)**2 == (v1.squared_length * v2.squared_length)):
        return False
    if (scalar_multiply(v2, v3) < 0) and (scalar_multiply(v2, v3)**2 == (v2.squared_length * v3.squared_length)):
        return False
    return (vector_multiply(v1, v2) * vector_multiply(v3, v2)) <= 0


a, b, c, d, e, f, g, h = list(map(int, input().split()))
if a == c:
    length = abs(b - d)
else:
    length = abs(a - c)
length /= 2
center = Point((a + c + e + g)/4, (b + d + f + h)/4)
a, b, c, d, e, f, g, h = list(map(int, input().split()))
points = [Point(a, b), Point(c, d), Point(e, f), Point(g, h)]
up_index = 0
for i in range(4):
    if points[i].y > points[up_index].y:
        up_index = i
up = points[up_index]
down = points[(up_index+2)%4]
right = points[(up_index+1)%4]
left = points[(up_index+3)%4]
if right.x < left.x:
    left, right = right, left
p = [
    Point(up.x - length, up.y + length),
    Point(up.x + length, up.y + length),
    Point(right.x + length, right.y + length),
    Point(right.x + length, right.y - length),
    Point(down.x + length, down.y - length),
    Point(down.x - length, down.y - length),
    Point(left.x - length, left.y - length),
    Point(left.x - length, left.y + length),
]
ans = check_angle(center, p[6], p[7], p[0]) & check_angle(center, p[7], p[0],
                                                          p[1])
for i in range(6):
    ans &= check_angle(center, p[i], p[i+1], p[i+2])
if ans:
    print("YES")
else:
    print("NO")
--------------------------------------------------------------------------
By Kapt, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (C) Two Squares, Accepted, #
 def sq(arr):
    y1, x1 = arr[0][0], arr[0][1]
    xa, ya = x1, y1
    cnt = 0
    for i in range(2):
        yb, xb = arr[i + 1][0], arr[i + 1][1]
        cnt += (xb - xa) * (ya + yb) / 2
        xa, ya = xb, yb
    cnt += (x1 - xa) * (y1 + ya) / 2
    return cnt

def inm(points, x, y):
    f = True
    for i in range(4 - 1, -1, -1):
        a, b, c = points[i], points[i - 1], points[i - 2]
        if not((sq([a, b, c]) >= 0 and sq([a, b, (x, y)]) >= 0) or (sq([a, b, c]) <= 0 and sq([a, b, (x, y)]) <= 0)):
            f = False
            break
    return f

read = lambda: map(float, input().split())
n = 4
points1 = []
arr = list(map(int, input().split()))
for i in range(4):
    points1.append((arr[i * 2 + 1], arr[i * 2]))
points2 = []
arr = list(map(int, input().split()))
for i in range(4):
    points2.append((arr[i * 2 + 1], arr[i * 2]))
for i in range(-100, 101):
    for j in range(-100, 101):
        if inm(points1, i, j) and inm(points2, i, j):
            print('YES')
            exit()
print('NO')
--------------------------------------------------------------------------
By KAin0, contest: Codeforces Round #488 by NEAR (Div. 2), problem: (C) Two Squares, Accepted, #
 mas = list(map(int, input().split()))
gas = list(map(int, input().split()))
x1 = list(set(mas[::2]))
y1 = list(set(mas[1::2]))
x2 = list(set(gas[::2]))
y2 = list(set(gas[1::2]))
g = min(x2) + (max(x2) - min(x2)) / 2
f = min(y2) + (max(y2) - min(y2)) / 2
d2 = max(y2) - min(y2)
if g >= min(x1) and g <= max(x1) and f >= min(y1) and f <= max(y1):
    print("YES")
    exit(0)
for i in range(0, 8, 2):
    v = gas[i]
    j = gas[i + 1]
    if v >= min(x1) and v <= max(x1) and j >= min(y1) and j <= max(y1):
        print("YES")
        exit(0)
for i in range(0, 8, 2):
    if abs(mas[i] - g) + abs(mas[i+1] - f) <= d2 / 2:
        print("YES")
        exit(0)
print("NO")
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
