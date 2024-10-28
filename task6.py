# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3

def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

m = int(input())
n = int(input())
c = nod(m,n)
m1 = m//c
n1 = n//c
print(m1, n1)