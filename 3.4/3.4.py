# #Задание 1

while True:
    n = int(input())
    if 1 <= n <= 100000:
        break
    else:
        print("Число n должно быть в диапазоне от 1 до 100000")

numbers = input().split()
unique_numbers = set()

for num in numbers:
    num = int(num)
    if -2 * 10**9 <= abs(num) <= 2 * 10**9:
        unique_numbers.add(num)
    else:
        print("Число должно не превышать по модулю 2*10^9")

print(len(unique_numbers))

#Задание 2

def elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return len(common_elements)

print("Введите числа первого списка:")
input_str = input()
list1 = list(map(int, input_str.split()[:100000]))  # Ограничение в 100000 чисел

print("Введите числа второго списка:")
input_str = input()
list2 = list(map(int, input_str.split()[:100000]))  # Ограничение в 100000 чисел

count = elements(list1, list2)

print("Количество чисел, содержащихся одновременно в обоих списках:", count)


# #Задание 3

numbers = input().split()

numb = set()

for number in numbers:
    if number in numb:
        print("YES")
    else:
        print("NO")
    numb.add(number)