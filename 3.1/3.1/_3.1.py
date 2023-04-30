#Задание 1

zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        zeroes += 1
print(zeroes)

#Задание 2

x = int(input())

if x == 1:
    d = 1
else:
    d = 2
    for i in range(2, int((x/2) + 1)):
        if x % i == 0:
            d += 1

print(d)

#Задание 3

a = int( input("Enter a: ") )
b = int( input("Enter b: ") ) + 1
 
[ print(num, end = " ") for num in range(a,b) if a<b and num%2 == 0]


#Test
######################################################
# clients = int(input())
# cards = int(input())
# while (clients > 0) and (cards >= 0):
#     print("How much are you buyin?")
#     howMuch = int(input())
#     clients -= 1
#     if cards >= howMuch:
#         cards -= howMuch


# a = int(input())
# b = int(input())
# for i in range(b, a-1, -1):
#     print(i)


# n = int (input())
# for i in range(n):
#     salary = int(input())
#     if salary % 2 == 0:
#         print(i+1,'Fired')
#     else:
#         print(i+1, 'All good')


######################################################