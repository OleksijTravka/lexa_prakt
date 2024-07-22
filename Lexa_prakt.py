import math



a  = input()
b  = input()
c  = input()
a = int(a)
b = int(b)
c = int(c)

p = pow(b, 2) - (a * c)
s = b + math.sqrt(p) / ( 2 * a)

print(s)
