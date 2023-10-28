#задача 1
# age = int(input("Введите ваш возраст: "))

# if age < 18:
#     print("ВЫ являетесь несовершеннолетным")
# elif age >= 18 and age <= 65:
#     print("Вы являетесь взрослым.")
# else: print("Вы являетесь пожилым")

#задача2
# num1 = float(input("первое число: "))
# num2 = float(input("второе число: "))
# num3 = float(input("третье число: "))

# if num1<num2 and num1<num3:
#     print(f"Hаименьшее число:{num1}")
# elif num2<num1 and num2<num3:
#     print(f"Hаименьшее число:{num2}")
# else:print(f"Hаименьшее число:{num3}")

#задача3
# list = ["osh","bishkek","chuy","talas","batken","mers","bugatti","car8","car9","car10","car11","car12","car13","car14","car15"]
# list2 = list[2:7]
# print(list2)

# list = ["osh","bishkek","chuy","talas","batken","mers","bugatti","car8","car9","car10"]
# list2 = list[2:9]
# print(list2)

# list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# list.pop(2)
# list.pop(16)
# list.insert(0,5)
# list.insert(1,9)
# print(list)

# numbers = [2, 3, 1, 52, 56, 8, 3, 58, 0, 98, 75, 3, 45, 21, 44, 2, 1, 4, 5, 6, 8, 909, 4, 24, 653, 12, 43, 2, 5, 8, 5, 3, 6, 8, 0, 2, 12, 4, 32, 5, 7, 43, 8, 0, 8, 654, 235, 65, 2, 3, 6, 0, 9, 8, 6, 43, 2, 4, 56, 2, 36, 7, 954, 2, 34, 6, 8, 45, 2, 4, 5, 73, 1, 32, 5, 321, 452, 3]
# numbers.sort()
# print(numbers)

#numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3]
# numbers.sort()
# numbers.reverse()
# print(numbers)

# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3]
# count_2 = numbers.count(2)
# count_5 = numbers.count(5)
# count_3 = numbers.count(3)
# print("Число 2 встречается", count_2, "раз")
# print("Число 5 встречается", count_5, "раз")
# print("Число 3 встречается", count_3, "раз")

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

my_list = list(range(1, 21))
average = sum(my_list) / len(my_list)
print("Среднее арифметическое:", average)


