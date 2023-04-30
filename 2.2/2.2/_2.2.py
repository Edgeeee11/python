#Задание 1
a, b = map(float, input().split())
S = a*b
P=2*a+2*b
print(S, P)

#Задание 2
number = float(input())
units = number % 10
dozens = number % 100 // 10
hundreds = number % 1000 // 100
thousands = number % 10000 // 1000
doz_of_thous = number // 10000
print((dozens ** units) * hundreds / (doz_of_thous - thousands))
print(units, dozens, hundreds, thousands, doz_of_thous)