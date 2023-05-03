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

word = input("Введите слово: ")

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for letter in word:
    if letter.lower() in vowels:
        vowel_count += 1
    elif letter.isalpha():
        consonant_count += 1

if vowel_count == 0 or consonant_count == 0:
    print("False")
else:
    print(f"В слове имеется {vowel_count} гластных и {consonant_count} согласных.")

#Задание 3

X = int(input())
A = int(input())
B = int(input())

if A >= X and B >= X:
    print(2)
elif A >= X and B < X:
    print("Mike")
elif A < X and B >= X:
    print("Ivan")
elif A + B >= X:
    print (1)
else:
    print(0)