# tmpp = 'absdf'
# print(tmpp[-1])
# s1 = 'asd'
# s2 = 'fgh'
# s3 = s1+s2
# print(s3)
# print(len(s3))
# s1 = 'abcdefghijk'
# print(s1[0:5:2])
# print(s1[5::-1])
# print(s1[5::1])
# print(s1[:5])
# print(s1[3:])
# tmp = [4, 3, 2, 9, 7]
# t2 = tmp [::2]
# print(tmp[::2])
# print(t2)

# tmp = "3 + 8 + 9 + 10"
# t = tmp.split(' + ')
# print(t)

# tmp = ['3', '4', '9', '157']
# print(' + '.join(tmp))

# name1 = input()
# name2 = input()
# print("Hello", name1)
# print(f'Hello, {name1}')
# test = f'Hello, {name1}'
# print(test)
# res = f'{name1}+{name2}=Love'
# print(res)

# s1 = 'sadafkjdslkgfaj'
# print(s1.upper())
# s1 = 'ASFASFASFSD'
# print(s1.lower())


# t = 'abzr'
# for c in t:
#     code = ord(c)+3
#     if code > 122:
#         print(chr(97 + code - 122), end ='')
#     else:
#         print(chr(code), end='')



#Задание 1
string = input()
if string == string[::-1]:
    print("yes")
else:
    print("no")