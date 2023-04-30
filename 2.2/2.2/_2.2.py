#Задание 1
a, b = map(float, input().split())
S = a * b
P = (2 * a) + (2 * b)
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



###
# a = 10 / 3 #Вещественное деление
# a = 7 // 5 # Целочисленное деление
# b = 7 % 5 #Деление с остатком (выводит только остаток)
# c = 2 ** 5 #Возведение в степень 2^5
# a += 10 #К переменной а добавляем 10 и переприсваеваем
# a, b = map(int, input().split()) #Для строки применяется метод map, который приводит элементы в ней к целочисленному значению int, split() просто разделяет строку по пробелу
# print(a, b)
###