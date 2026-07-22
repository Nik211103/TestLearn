h = int(input("Введите желаемую высоту треугольника: "))

for i in range(1, h + 1):
    space = " "  *  (h - i)
    plus = "+" * (2 * i - 1)
    print(space + plus)    