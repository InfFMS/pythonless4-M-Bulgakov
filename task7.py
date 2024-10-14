# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.

def t(a, b, c):
    if a + b>c and a +c > b and b +c >a:
        return True
    else:
        return False

print(t(int(input()),int(input()),int(input())))