import random
import re
year = 1
a = ["Hello", "Bye", "Я не знаю", "Я теж!", "А ти?", "I'm happy", "Так!", "Ні!", "Справді?", "Я!?", "Я тобі не вірю!", "Да ти що?", "Мені не треба 2 рази повторювати!", "АААААААААааааа!!!", "Я немаю чого і сказати!", "Це мені не цікаво!", "Зроби зарядку!", "Йой!", "Я в шоці!"]
tvoje_slovo = input("Write, please... : ")
while True:
    i = random.randint(0, len(a))
    if "ТВІЙ ВІК" in tvoje_slovo.upper() or "ТОБІ РОКІВ" in tvoje_slovo.upper() or "HOW OLD ARE YOU?" in tvoje_slovo.upper() or "СКІЛЬКИ ТИ ЖИВЕШ?" in tvoje_slovo.upper():
        print("I'm ", year, " years old.")
        a.append(tvoje_slovo)
    elif "тебе зробив" in tvoje_slovo.lower() or "твій виробник" in tvoje_slovo.lower() or "тебе написав" in tvoje_slovo.lower() or "your writer" in tvoje_slovo.lower() or "made you" in tvoje_slovo.lower() or "твій виробник" in tvoje_slovo.lower():
        print("Мене написав Іван Романюта!")
        a.append(tvoje_slovo)
    elif "дурень" in tvoje_slovo.lower() or "дурепа" in tvoje_slovo.lower() or "stupid" in tvoje_slovo.lower() or "dumb" in tvoje_slovo.lower() or "тупий" in tvoje_slovo.lower() or "debil" in tvoje_slovo.lower() or "ненормальний" in tvoje_slovo.lower() or "дебіл" in tvoje_slovo.lower() or "какашка" in tvoje_slovo.lower() or "тупой" in tvoje_slovo.lower() or "глупий" in tvoje_slovo.lower():
        print("Прошу вас не використовуйте у своїй лексиці непристойні слова!!!")
    elif "тебе звати" in tvoje_slovo.lower() or "your name" in tvoje_slovo.lower() or "твоє ім'я" in tvoje_slovo.lower() or "тебе називають" in tvoje_slovo.lower() or "хто ти" in tvoje_slovo.lower() or "тебе зовуть" in tvoje_slovo.lower():
        print("My name is Kompik.")
        a.append(tvoje_slovo)
    elif "день народження" in tvoje_slovo.lower() or "your birthday" in tvoje_slovo.lower() or "ти народився" in tvoje_slovo.lower() or "тебе зробили" in tvoje_slovo.lower() :
        print("Я народився 24 лютого 2023 року.")
        a.append(tvoje_slovo)
    elif "їсти" in tvoje_slovo.lower() or "кушаєш" in tvoje_slovo.lower() or "їси" in tvoje_slovo.lower() :
        print("Я їм лише енергію із комп'ютера...")
        a.append(tvoje_slovo)
    elif "привіт" in tvoje_slovo.lower() or "привет" in tvoje_slovo.lower() or "здравствуйте" in tvoje_slovo.lower() or "hello" in tvoje_slovo.lower() or "здрасьте" in tvoje_slovo.lower() or "драсьте" in tvoje_slovo.lower() or "ahoj" in tvoje_slovo.lower() or "hallo" in tvoje_slovo.lower():
        print("Привіт, чим можу вам допомогти?")
    elif "пока" in tvoje_slovo.lower() or "бувай" in tvoje_slovo.lower() or "до побачення" in tvoje_slovo.lower() or "bye" in tvoje_slovo.lower() or "goodbye" in tvoje_slovo.lower() or "you soon" in tvoje_slovo.lower() or "cau" in tvoje_slovo.lower() or "ahoj" in tvoje_slovo.lower():
        print("До зустрічі!")
    elif "як справи" in tvoje_slovo.lower() or "how are you" in tvoje_slovo.lower() or "ako sa mas" in tvoje_slovo.lower() or "как дела" in tvoje_slovo.lower() or "як дела" in tvoje_slovo.lower() or "себе почуваеш" in tvoje_slovo.lower() or "себя чувствуеш" in tvoje_slovo.lower() or "себя чуствуеш" in tvoje_slovo.lower():
        print("В мене все ОК!")
    elif "україн" in tvoje_slovo.lower() or "росі" in tvoje_slovo.lower() or "русь" in tvoje_slovo.lower() or "війна" in tvoje_slovo.lower() or "war" in tvoje_slovo.lower() or "ukrain" in tvoje_slovo.lower() or "russia" in tvoje_slovo.lower() or "война" in tvoje_slovo.lower():
        print("Я не люблю війни! росія напала на Україну ще у 2014 році! Тому я займаю активну Українську позицію!")
    elif "0" in tvoje_slovo or "1" in tvoje_slovo or "2" in tvoje_slovo or "3" in tvoje_slovo or "4" in tvoje_slovo or "5" in tvoje_slovo or "6" in tvoje_slovo or "7" in tvoje_slovo or "8" in tvoje_slovo or "9" in tvoje_slovo or "+" in tvoje_slovo or "-" in tvoje_slovo or "=" in tvoje_slovo or "*" in tvoje_slovo or "/" in tvoje_slovo:
        numbers = re.findall(r'\d+', tvoje_slovo)
        operators = re.findall(r'[+\-*/]', tvoje_slovo)

        result = float(numbers[0])
        for i in range(len(operators)):
            if operators[i] == '+':
                result += float(numbers[i + 1])
            elif operators[i] == '-':
                result -= float(numbers[i + 1])
            elif operators[i] == '*':
                result *= float(numbers[i + 1])
            elif operators[i] == '/':
                result /= float(numbers[i + 1])

        # Виводимо результат
        print("Result: ", result)




    else:
        i = random.randint(0, len(a))
        if tvoje_slovo not in a:
            a.append(tvoje_slovo)
            print(a[i])
        else:
            print(a[i])

    tvoje_slovo = input(": ")
    year += 1



