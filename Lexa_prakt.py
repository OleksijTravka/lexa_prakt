import math

a = input()
a = int(a)

first = a % 10
second = math.floor(a / 10) % 10
third = math.floor(a / 100) % 10

print(first)
print(second)
print(third)
print(first + second + third)
