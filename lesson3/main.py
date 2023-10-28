# if - если, elif - если , else - иначе


# name = 'Nurbolot'
# age = 17
# #здравствуйте Nurbolot, вам 17 лет.
# print('здравствуйте', name ,  'вам', age , 'лет' )
# print(f"здравствуйте {name}, вам {age} лет")

# num1 = 20
# num2 = 100
# num3 = 600
# if num1 > num2 and num1 > num3:
#     print(f"{num1} больше {num2} так же {num3}")
# elif num3 >num2 and num3 > num1:
#     print(f"{num3} больше {num2} так же {num1}")
# else:
#     print(f"{num2} больше {num1} ")

# nbers = [1,2,3,4,5,6,7,8,9,10,5]
# print(numbers)um
# user = ["Bishkek", "asia", "batken" ]
# users = ["Geeks", "Osh" , "Antona", "Nurbolot"]
# print(users)
# users.append("Beksultan")  #для добавления в конец списка
# print(users)
# users.insert(0, "Kyrgyzstan") # для добавления по индексу
# print(users)
# users.remove("Antona") #для удаления по названию
# print(users)
# users.pop(3) #для удаления по индексу
# print(users)
# users.extend(user) #для обьеденения
# print(users)
# users.sort() #сортировка
# print(users)
# users.reverse() #перевернуть
# print(users)
# # users.clear() #очистит
# print(users)
# users_copy = users.copy() #copiya
# print(users_copy)
# print(users.index("Beksultan")) #index
# print(users.count("Geeks")) # kolichestvo 


# numbers = ["2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,"]
# numbers.sort()
# print(numbers)



# from random import randint


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))


# def new_func1(x, y):
    
#     print(56)

# def new_func(a, b):
   
#     return new_func1(a, b)


# c = new_func(a, b)
# print(c)

string1 = "Aidana"
string2 = "Adilet"

result = ""

# Проходим по символам строк с использованием цикла
for char1, char2 in zip(string1, string2):
    result += char1 + char2

# Если одна из строк короче другой, добавляем оставшиеся символы
if len(string1) > len(string2):
    result += string1[len(string2):]
elif len(string2) > len(string1):
    result += string2[len(string1):]

print(result)