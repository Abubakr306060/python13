def chat_bot():
    while True:
        input_text = input("Введите ваш вопрос или сообщение: ")
        if input_text is None:
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        elif input_text.isupper():
            print("Успокойся")
        elif input_text.endswith('?'):
            print("Конечно!")
        else:
            print("Ну и что")


# chat_bot()

def phrase():
    word = input("введите слово")
    split_word = word.split()
    print(split_word)
    res = ""
    for s in split_word:
        res += s[0].upper()
    print(res)


# phrase()

def n():
   n_str = str(n)


