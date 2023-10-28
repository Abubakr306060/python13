# #functions - функции Python
# def hello():
#     print("hello world")
# hello() #вызов функции по имени hello()

def add():
    num1 = input("ввведите первое число: ")
    num2 = input("введите второе число: ")
    print(int(num1) + int(num2))
add()

# def reverse_name():
#     name = input("введите свое имя: ")
#     print(name[::-1])
# # reverse_name()

# print(len("hello"))
# print(len([1, "hello", True, 0.1]))

def sub(num1,num2): #num, num2 - параметры функции
    print(num1- num2)
# sub(20,10) #20, 10 - argumenti funksii
# sub(100,88)
# sub(100,200)

# def calculator(num1, num2, operator):
#     if operator == "+":
#         print(num1+num2)
#     elif operator == "-":
#         print(num1-num2)
#     elif operator == "*":
#         print(num1*num2)
#     elif operator == "/":
#         print(num1/num2)
#     else:
#         print("Такого оператора нету")

# calculator(10,50, '+')
# calculator(200,100, '-')
# calculator(100,30, '*')
# calculator(500,2, '/')

# def div(num1:int, num2:int):
#     try:
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("деление на ноль нельзя!!!")
# div(10,2)
# div(100,0)
# div(10.0, 3.0)

# def mult(num1:int=10, num2:int=10)-> int:
#     "это функция для умножуние чисел num1 и num2"
#     print(num1*num2)
# mult(20)





