import random
year = 1
a = ["Hello", "Bye", "My name is Kompik.", "Я теж!", "А ти?", "I'm happy", "Так!", "Ні!", "Справді?", "Я?", "Я тобі не вірю!", "Да ти що?", "Мені подобається борщ.", "АААААААААааааа!!!", "Я немаю чого і сказати!", "Це мені не цікаво!", "Зроби зарядку!", "Йой!", "Я в шоці!"]
tvoje_slovo = input("Write, please... : ")
while True:
    i = random.randint(0, len(a))
    if tvoje_slovo == "Твій вік" or tvoje_slovo == "Скільки тобі років?" or tvoje_slovo == "Kolko mas rokov?" or tvoje_slovo == "How old are you?" or tvoje_slovo == "Скільки ти живеш?":
        print("I'm ", year, " years old.")
        a.append(tvoje_slovo)
    elif tvoje_slovo == "Хто тебе зробив?" or tvoje_slovo == "Хто твій виробник?" or tvoje_slovo == "Хто тебе написав?" or tvoje_slovo == "Who is your writer?" or tvoje_slovo == "Who is made you?" :
        print("Мене написав Іван Романюта!")
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



