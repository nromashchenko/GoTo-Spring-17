import math
from GoToMath import distance


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

print("distance1: ", distance(x1, y1, x2, y2))
print("distance2: ", distance(x1, y1, x3, y3))
print("distance3: ", distance(x3, y3, x2, y2))
