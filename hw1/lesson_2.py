# #строки и методы строк
# #есть 4 вида строк
# str_one = 'Hello. I\'m Kurmanbek'
# print(str_one)
# str_two = "Hello World. I'm Kurmanbek.\n My language Python"
# print(str_two)

# str_three = """Hello World. I'm Kurmanbek
# My language Python"""
# print(str_three)

# str_four = '''Hello World. I'm Kurmanbek
# My language Python'''
# print(str_four)

# name = "Nurbolot"
# surname = "Erkinbaev"
# print(surname + " " + name) #канкатинация - сложение строк
# print("здравствуйте," + " " + name + " " + surname)
# print("здравствуйте,", name, surname)

# name = input("Имя: ")
# surname = input("Фамилия: ")
# print("здравствуйте,", name, surname)

# number1 = input(("введите первое число: "))
# number2 = input(("введите второе число: "))
# print("Ответ:", int(number1) + int(number2))

# it = "Geeks"
#      #01234
# print(it)
# print(it[0]) #индексы
# print(it[4])
# print(it[3])
# print(it[5])

# #срезы
# language = "python"
#            #012345
# print(language)
# print(language[0:2]) #начало : конец (до)
# print(language[2:6])
# print(language[::2])#начало : конец : шаг

# name = "kurmanbek"
# print(name)
# print(name[::-1]) #переворачиваем строку

# #Методы строк
# name = "nurBek"
# print(name.title())
# print(name.upper())
# print(name.upper())
# print(name.count('n'))




# Получаем слово от пользователя
word = input("Введите слово: ")


    # Выводим первую букву
print("Первая буква:", word[0])

    # Выводим последнюю букву
print("Последняя буква:", word[-1])

    # Выводим все буквы между первой и последней (включая их)
print("Буквы между первой и последней:", word[1:-1])
