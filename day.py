import random
import time
print("Це дуже цікава гра. Розвиває фінансову грамотність. Правила:"
      "Ти задаєш собі бюджет на день. І вибираєш день неділі. А далі розподіляєш свій бюджет на весь день. Це цікаво!!!")

print("1)Понеділок;"
      " 2)Вівторок;"
      " 3)Середа;"
      " 4)Четвер;"
      " 5)П'ятниця;"
      " 6)Субота;"
      " 7)Неділя.")


day_today = int(input("Введи цифру дня:"))
if day_today<1 or day_today>7:
    day_today = random.randint(1, 7)
    print("Неправильний день неділі! Зараз ",day_today,"-ий день неділі")
else:
    print("Вірний день неділі!")



your_money = int(input("Твій бюджет(1$ - 1000$) : "))
if your_money<1 or your_money>1000:
    print("Неправильний бюджет! В тебе 50$!")
    your_money = 50
else:
    print("Вірний бюджет!")





if day_today>=1 and day_today<=2:
    print("Ти прийшов у магазин. Що тобі треба купити?")
    time.sleep(1)
    a = int(input("1)Овочі - 5$;"
          " 2)Фрукти - 5$;"
          " 3)Молочні продукти - 3$;"
          " 4)Кондитерські вироби - 7$;"
          " 5)Хліб - 3$;"
          " 6)Крупи - 5$: "))

    if a == 1 or a == 2 or a == 6:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ",your_money, "$")
    if a == 5 or a == 3:
        print("З вас 3$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 3
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ",your_money, "$")
    if a == 4 :
        print("З вас 7$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 7
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ",your_money, "$")
        time.sleep(1.5)



    print("Ти прийшов у магазин одежі. Що тобі треба купити?")
    time.sleep(1)
    a = int(input("1)Нові джинси - 55$;"
                      " 2)Кросівки - 160$;"
                      " 3)Модна курточка - 35$;"
                      " 4)Шапку - 5$;"
                      " 5)Аксесуари - 5$;"
                      " 6)Спортивний костюм - 35$: "))

    if a == 3 or a == 6:
        print("З вас 35$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 35
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 5 or a == 4:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 1:
        print("З вас 55$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 55
                break
            else:
                print("Спробуйте ще раз!")
    if a == 2:
        print("З вас 160$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 160
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
        time.sleep(1.5)

    print("Ти прийшов у Піцерію 'Le Morkvopizza'. Яку піцу хочете купити?")
    time.sleep(1)
    a = int(input("1)Маргарита - 5$;"
                          " 2)Чотири сира - 7$;"
                          " 3)Чотири м'яса - 5$;"
                          " 4)Баварська - 7$;"
                          " 5)Грибна - 8$;"
                          " 6)М'ясна - 8$ : "))
    if a == 5 or a == 6:
        print("З вас 8$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 8
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 2 or a == 4:
        print("З вас 7$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 7
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 1 or a == 3:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
        time.sleep(1.5)





elif day_today>=3 and day_today<=5:
    print("Ти прийшов у магазин одежі. Що тобі треба купити?")
    time.sleep(1)
    a = int(input("1)Нові джинси - 55$;"
          " 2)Кросівки - 160$;"
          " 3)Модна курточка - 35$;"
          " 4)Шапку - 5$;"
          " 5)Аксесуари - 5$;"
          " 6)Спортивний костюм - 35$: "))

    if a == 3 or a == 6:
        print("З вас 35$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 35
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ",your_money, "$")
    if a == 5 or a == 4:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ",your_money, "$")
    if a == 1 :
        print("З вас 55$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 55
                break
            else:
                print("Спробуйте ще раз!")
    if a == 2:
        print("З вас 160$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 160
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
        time.sleep(1.5)


    print("Ти прийшов у магазин. Що тобі треба купити?")
    time.sleep(1)
    a = int(input("1)Овочі - 5$;"
                      " 2)Фрукти - 5$;"
                      " 3)Молочні продукти - 3$;"
                      " 4)Кондитерські вироби - 7$;"
                      " 5)Хліб - 3$;"
                      " 6)Крупи - 5$: "))

    if a == 1 or a == 2 or a == 6:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 5 or a == 3:
        print("З вас 3$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 3
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 4:
        print("З вас 7$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 7
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
        time.sleep(1.5)



    print("Ти прийшов у Піцерію 'Le Morkvopizza'. Яку піцу хочете купити?")
    time.sleep(1)
    a = int(input("1)Маргарита - 5$;"
                      " 2)Чотири сира - 7$;"
                      " 3)Чотири м'яса - 5$;"
                      " 4)Баварська - 7$;"
                      " 5)Грибна - 8$;"
                      " 6)М'ясна - 8$ : "))
    if a == 5 or a == 6:
        print("З вас 8$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 8
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 2 or a == 4:
        print("З вас 7$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 7
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 1 or a == 3:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
        time.sleep(1.5)





else:
    print("Ти прийшов у Піцерію 'Le Morkvopizza'. Яку піцу хочете купити?")
    time.sleep(1)
    a = int(input("1)Маргарита - 5$;"
                  " 2)Чотири сира - 7$;"
                  " 3)Чотири м'яса - 5$;"
                  " 4)Баварська - 7$;"
                  " 5)Грибна - 8$;"
                  " 6)М'ясна - 8$ : "))
    if a == 5 or a == 6:
        print("З вас 8$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 8
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ",your_money, "$")
    if a == 2 or a == 4:
        print("З вас 7$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 7
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ",your_money, "$")
    if a == 1 or a == 3:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ",your_money, "$")
        time.sleep(1.5)




    print("Ти прийшов у магазин одежі. Що тобі треба купити?")
    time.sleep(1)
    a = int(input("1)Нові джинси - 55$;"
                      " 2)Кросівки - 160$;"
                      " 3)Модна курточка - 35$;"
                      " 4)Шапку - 5$;"
                      " 5)Аксесуари - 5$;"
                      " 6)Спортивний костюм - 35$: "))

    if a == 3 or a == 6:
        print("З вас 35$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 35
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 5 or a == 4:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 1:
        print("З вас 55$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 55
                break
            else:
                print("Спробуйте ще раз!")
    if a == 2:
        print("З вас 160$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 160
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
        time.sleep(1.5)


    print("Ти прийшов у АТБ. Що тобі треба купити?")
    time.sleep(1)
    a = int(input("1)Овочі - 5$;"
                          " 2)Фрукти - 5$;"
                          " 3)Молочні продукти - 3$;"
                          " 4)Кондитерські вироби - 7$;"
                          " 5)Хліб - 3$;"
                          " 6)Крупи - 5$: "))

    if a == 1 or a == 2 or a == 6:
        print("З вас 5$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 5
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 5 or a == 3:
        print("З вас 3$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 3
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
    if a == 4:
        print("З вас 7$")
        perev1 = 0
        while perev1 <= 1:
            perev1 = int(input("Підтверджуєте свій вибір? 1-так; 0-ні."))
            if perev1 == 1:
                print("Добре")
                your_money -= 7
                break
            else:
                print("Спробуйте ще раз!")
        print("В тебе залишилось ", your_money, "$")
        time.sleep(1.5)












