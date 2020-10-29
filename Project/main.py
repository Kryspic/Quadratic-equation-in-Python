import math
import odds
import diskriminant
a, b, c = odds.odds()
a = int(a)
b = int(b)
c = int(c)

print("Choose a variation of the solution:\n1. Diskriminant\n2. Viet")
variation = input()
if variation == "1" or "2" or "Diskriminant" or "Viet":
    diskriminant.discriminant(a, b, c)
