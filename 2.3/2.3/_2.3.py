#Задание 1

number = int(input())

if (number < 0) and ( number%2 == 0 ):
    print("Отрицательное четное число")
elif (number < 0) and ( number%2 != 0 ):
    print("Отрицательное нечетное число")
elif (number > 0 ) and ( number%2 == 0 ):
    print("Положительное четное число")
elif (number > 0 ) and ( number %2 != 0 ):
    print("Положительное нечетное число")
else:
    print("Нулевое число")

#Задание 2
get_len = lambda user_str: sum(user_str.count(i) for i in user_str)
get_vowels = lambda user_str: sum(user_str.count(i) for i in 'aeiouy')
user_str = input("Enter Sentence")
print (get_vowels(user_str))

#Задание 3
X = int(input())
A = int(input())
B = int(input())

if A and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print (1)
else:
    print(0)