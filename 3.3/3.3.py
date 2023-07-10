# #Задание 1

n = int(input("Enter the number of elements (1 <= N <= 10000): "))
if n < 1 or n > 10000:
    print("Invalid value for N")
    exit()

a = []

for i in range(n):
    number = int(input(f'Enter number {i+1}: '))
    if -10**5 <= number <= 10**5:
        a.append(number)
    else:
        print('Number is less than -10^5 or more than 10^5')
        exit()

a.reverse()

for number in a:
    print(number)

#Задание 2

def shift(arr):
    return [arr[-1]] + arr[:-1]

num = int(input())
nums = list(map(int, input().split()))

if len(nums) != num:
    print("Error: Number of integers entered does not match the value of num")
    exit()

for num in nums:
    if num <1 or num > 10**9:
        print("Error: Number must be between 1 and 10^9")
        exit()

changed_array = shift(nums)

for num in changed_array:
    print(num, end=' ')

#Задание 3

m = int(input("Mass: "))
if not 1 <= m <= 10**6:
    print("Invalid input for m.")
    exit()
n = int(input("Number of fisherman: "))
if not 1 <= n <= 100:
    print("Invalid input for n.")
    exit()
weights = []
for i in range(n):
    Ai = int(input(f"Weight {i+1}: "))
    if not 1 <= Ai <= m:
        print("Invalid input for weight.")
        exit()
    weights.append(Ai)

weights.sort()
boats = 0
a = 0
b = n - 1

while a <= b:
    if weights[b] + weights[a] <= m:
        a += 1
    b -= 1
    boats += 1

print(boats)









# a = [3, 4, 9, 1, 4, 3, 2, 3, 3 ,3]
# a[1] = 10
# print(a[1])#Отображение по индексу
# a.append(190)#Добалвение элемента в конец массива
# print(a[-1])#Обратная индексация (отображает последний элемент)
# print(len(a))#Отображение длины массива
# print(*a)#Отображение всех элементов массива в строку
# a.insert(3, 99)#Добавление элемента в место по индексу (номер элемента, значение)
# print(*a)
# a.pop()#Удаление последнего элемента в массиве
# print(*a)
# a.pop(1)#Удаление элемента по индексу
# print(*a)
# # a.clear()#Очистка массива
# # print(*a)
# a.reverse()#Переворачивает список задом наперед
# print(*a)
# print(a.count(3))#Подсчитывает колличество элементов, равному значению 3

# n = int(input())
# res = []
# for i in range(n):
#     a = int(input())
#     res.append(a)
# print(res)           #Введение значений через Enter


# res = list(map(int, input().split())) #Вывод массива через пробелы
# print(res)           


# tmp = list(map(int, input().split()))
# res = []
# for i in range(len(tmp)):
#     if tmp[i] != 50:
#         res.append(tmp[i])
# print(res)                #Перебор элементов списка по индексу



# tmp = list(map(int, input().split()))
# res = []
# for i in tmp:
#     if i !=50:
#         res.append(i)
# print(res)               #Перебор элементов списка по значению списка

# a = [3 for i in range(100)] #Цикл для бобавления 100 элементов цифры 3
# print(a)
# print(len(a))

# a = 5
# b = a
# a = 7
# print(b)