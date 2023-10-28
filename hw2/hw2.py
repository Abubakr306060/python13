"""ЗАДАЧА №1
Напишите программу, которая принимает строку от пользователя и выводит её в
обратном порядке.
ЗАДАЧА №2
Напишите программу, которая принимает слово от пользователя и выводит
информацию о нем: первую букву, последнюю букву и все буквы между первой и
последней (включая их).
ЗАДАЧА №3
Вам дается текст:
Advertising companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children’s ‘pester
power’ to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money.
Посчитайте количество букв s и t .
ДОП ЗАДАЧА:
Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную
строку из двух имен, буква за буквой.
Результат: "AAiddialnea"""

###111
str = input("Введите строку: ")

rev_str = str[::-1]
print("Строка в обратном порядке:", rev_str)


###222
word = input("Введите слово: ")

first = word[0]
print("Первая буква:", first)

last = word[-1]
print("Последняя слова:", last)

between = word[1:-1]
print("Буквы между первой и последней:", between)

###333
text = """Advertising companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children’s ‘pester
power’ to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money.
Посчитай"""

s = text.count('s')
t = text.count('t')

print("Количество букв 's' в тексте:", s)
print("Количество букв 't' в тексте:", t)

####4444

