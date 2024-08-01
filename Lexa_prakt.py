a = input()
a = int(a)

first = a % 10
second = round(a / 10) % 10
third = round(a / 100) % 10

print(first + second + third)
