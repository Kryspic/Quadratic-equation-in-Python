import math
def discriminant(a, b, c):
    if b % 2 == 0:
        diskr = math.sqrt(b**2 - (a * c))
        x1 = (-b + diskr) / 2 * a
        x2 = (-b - diskr) / 2 * a
        print(x1, x2)
    else:
        diskr = math.sqrt(b**2 - 4*(a * c))
        x1 = (-b + diskr) / 2 * a
        x2 = (-b - diskr) / 2 * a
        print(x1, x2)
