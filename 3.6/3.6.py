#Задание 1

def calc(n):
    fac = 1
    list = []

    for i in range(1, n + 1):
        fac *= i
        list.append(fac)

    list.reverse()
    return fac, list

number = int(input("Введите натуральное целое число: "))

fac, list = calc(number)
print("Факториал числа", number, ":", fac)
print("Список факториалов:", list)

#Задание 2

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def create():
    last_key = max(pets.keys())
    pet_id = last_key + 1 if pets else 1

    name = input("Введите имя питомца: ")
    type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[pet_id] = {
        name: {
            "Вид питомца": type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }

    print("Запись успешно добавлена.")

def read():
    id = int(input("Введите ID питомца: "))
    info = pets.get(id)

    if info:
        name = list(info.keys())[0]
        type = info[name]["Вид питомца"]
        age = info[name]["Возраст питомца"]
        owner = info[name]["Имя владельца"]

        suffix = get_suffix(age)
        print(f"Это {type} по кличке \"{name}\". Возраст питомца: {age} {suffix}. Имя владельца: {owner}")
    else:
        print("Питомец с указанным ID не найден.")

def update():
    id = int(input("Введите ID питомца: "))
    info = pets.get(id)

    if info:
        name = list(info.keys())[0]

        type = input("Введите новый вид питомца: ")
        age = int(input("Введите новый возраст питомца: "))
        owner = input("Введите новое имя владельца: ")

        info[name]["Вид питомца"] = type
        info[name]["Возраст питомца"] = age
        info[name]["Имя владельца"] = owner

        print("Запись успешно обновлена.")
    else:
        print("Питомец с указанным ID не найден.")

def delete():
    id = int(input("Введите ID питомца: "))
    info = pets.get(id)

    if info:
        del pets[id]
        print("Запись успешно удалена.")
    else:
        print("Питомец с указанным ID не найден.")

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "года"
    else:
        return "лет"

def pets_list():
    for id, info in pets.items():
        name = list(info.keys())[0]
        type = info[name]["Вид питомца"]
        age = info[name]["Возраст питомца"]
        owner = info[name]["Имя владельца"]

        suffix = get_suffix(age)
        print(f"ID: {id}. {type} по кличке \"{name}\". Возраст питомца: {age} {suffix}. Имя владельца: {owner}")

command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ")

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Программа завершена.")
    else:
        print("Неверная команда. Повторите попытку.")