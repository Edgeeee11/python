#Задание 1

def a(list, index=0):
    if index < len(list):
        print(list[index])
        a(list, index + 1)
    else:
        print("Конец списка")

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
a(list)
