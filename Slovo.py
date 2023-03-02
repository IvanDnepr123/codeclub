import random
year = 1
a = ["Hello", "Bye", "Я не знаю", "Я теж!", "А ти?", "I'm happy", "Так!", "Ні!", "Справді?", "Я!?", "Я тобі не вірю!", "Да ти що?", "Мені не треба 2 рази повторювати!", "АААААААААааааа!!!", "Я немаю чого і сказати!", "Це мені не цікаво!", "Зроби зарядку!", "Йой!", "Я в шоці!"]
tvoje_slovo = input("Write, please... : ")
while True:
    i = random.randint(0, len(a))
    if "Твій вік" in tvoje_slovo or "тобі років" in tvoje_slovo  or "mas rokov" in tvoje_slovo  or "How old are you?" in tvoje_slovo  or "Скільки ти живеш?" in tvoje_slovo :
        print("I'm ", year, " years old.")
        a.append(tvoje_slovo)
    elif "тебе зробив" in tvoje_slovo or "твій виробник" in tvoje_slovo  or "тебе написав" in tvoje_slovo or "your writer" in tvoje_slovo or "made you" in tvoje_slovo :
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
    elif "будеш їсти" in tvoje_slovo.lower() or "йди їсти" in tvoje_slovo.lower() or "кушаєш" in tvoje_slovo.lower() or "їси" in tvoje_slovo.lower() :
        print("Я їм лише енергію із комп'ютера...")
        a.append(tvoje_slovo)
    else:
        i = random.randint(0, len(a))
        if tvoje_slovo not in a:
            a.append(tvoje_slovo)
            print(a[i])
        else:
            print(a[i])

    tvoje_slovo = input(": ")
    year += 1



