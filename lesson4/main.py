#Типы данных
#int, float, str, bool, list, tuple
#Tuple - кортежи
# names = ("Kurmanbek", "Nurbolot", "Beksultan")
# print(names)
# print(type(names))
# print(names.count("Beksultan"))
# print(names.index("Nurbolot"))

# tup = (10, 2.0, "Hello", True)
# print(tup)

# cars = ["BMW", "Tesla", "BYD", "Lexus"]
# tuple_cars = ("Cherry", "Haval", "Zeekr")
# print(cars + list(tuple_cars))

# it = ("Google", "Geeks", "Meta", "Amazon")
# print(it)
# print(it[1][0])
# print(it[1:3:1]) #срезы в кортежах (начало, конец, шаг)

# lst_it = list(it) #Преобразование tuple > list
# print(lst_it)
# lst_it.append("Pentagon")
# print(lst_it)

# it = tuple(lst_it)
# print(it)

#Исключения try, except
# try:
#     print(100 / 0)
# except ZeroDivisionError:
#     print("Делить число на ноль нельзя!")

# try:
#     print(2000 + 1000)
#     print(name)
# except TypeError:
#     print("Нельзя сложить типы данных int + str")
# except NameError:
#     print("Название перменной не найдено")