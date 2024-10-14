# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

#import math
#def nod(a,b)
#    return math.gcd(a,b)

print(f'НОД: {nod(int(input()),int(input()))}')