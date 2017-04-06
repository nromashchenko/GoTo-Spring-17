import math


def distance(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d

def fact(n):
    result = 1
    for i in range(1,n):
        result *= i
    return result
if __name__ == "__main__":
    print("Hello I am Math")