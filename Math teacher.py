import random
import time

level = 1
while True:
    if level == 1:
        cislo01 = random.randint(1,10)
        cislo02 = random.randint(1, 10)
        print (" " , cislo01 , " + ", cislo02 , " = ")
        a = int(input(" "))
        if a == cislo01 + cislo02:
            print("Hooray!!! It's correct! You're at the next 2 level!")
            level +=1


    if level == 2:
        cislo01 = random.randint(1,100)
        cislo02 = random.randint(1, 100)
        print (" " , cislo01 , " + ", cislo02 , " = ")
        a = int(input(" "))
        if a == cislo01 + cislo02:
            print("Hooray!!! It's correct! You're at the next 3 level!")
            level +=1
        else:
            print("Oops... It's not correct( You're at the 1 level")
            level -= 1



    if level == 3:
        cislo01 = random.randint(1,10)
        cislo02 = random.randint(1, 10)
        print (" " , cislo01 , " * ", cislo02 , " = ")
        a = int(input(" "))
        if a == cislo01 * cislo02:
            print("Hooray!!! It's correct! You're at the next 4 level!")
            level +=1
        else:
            print("Oops... It's not correct( You're at the 2 level")
            level -= 1


    if level == 4:
        cislo01 = random.randint(1, 1000)
        cislo02 = random.randint(1, 1000)
        print (" " , cislo01 , " + ", cislo02 , " = ")
        a = int(input(" "))
        if a == cislo01 + cislo02:
            print("Hooray!!! It's correct! You're at the next 5 level!")
            level +=1
        else:
            print("Oops... It's not correct( You're at the 3 level")
            level -= 1



    if level == 5:
        cislo01 = random.randint(1,10)
        cislo02 = random.randint(5, 100)
        print (" " , cislo01 , " * ", cislo02 , " = ")
        a = int(input(" "))
        if a == cislo01 * cislo02:
            print("Hooray!!! It's correct! You're at the next 6 level!")
            level +=1
        else:
            print("Oops... It's not correct( You're at the 4 level")
            level -= 1


    if level == 6:
        cislo01 = random.randint(1, 10)
        cislo02 = random.randint(1, 10)
        print (" " , cislo01 , " ^ ", cislo02 , " = ")
        a = int(input(" "))
        if a == cislo01 ** cislo02:
            print("Hooray!!! It's correct! You're at the next 7 level!")
            level +=1
        else:
            print("Oops... It's not correct( You're at the 5 level")
            level -= 1



    if level == 7:
        cislo01 = random.randint(1,100)
        cislo02 = random.randint(1, 100)
        print (" " , cislo01 , " * ", cislo02 , " = ")
        a = int(input(" "))
        if a == cislo01 * cislo02:
            print("Hooray!!! It's correct! You're at the next 8 level!")
            level +=1
        else:
            print("Oops... It's not correct( You're at the 6 level")
            level -= 1



    if level == 8:
        cislo01 = random.randint(1,100)
        cislo02 = random.randint(1, 100)
        cislo03 = random.randint(1, 10)
        print(" (", cislo01, " + ", cislo02 , ") * ", cislo03)
        a = int(input(" "))
        if a == (cislo01 + cislo02)*cislo03:
            print("Hooray!!! It's correct! You're at the next 9 level!")
            level +=1
        else:
            print("Oops... It's not correct( You're at the 7 level")
            level -= 1


    if level == 9:
        cislo01 = random.randint(5,10)
        cislo02 = random.randint(5, 20)
        cislo03 = random.randint(5, 10)
        cislo04 = random.randint(5, 20)
        print(" (", cislo01, " + ", cislo02 , ") * (", cislo03, "+", cislo04, ") = ")
        a = int(input(" "))
        if a == (cislo01 + cislo02)*(cislo03+cislo04):
            print("Hooray!!! It's correct! You're at the next 10 level!")
            level +=1
        else:
            print("Oops... It's not correct( You're at the 8 level")
            level -= 1


    if level == 10:
        cislo01 = random.randint(5,10)
        cislo0_01 = random.randint(1, 10)
        cislo02 = random.randint(5, 20)
        cislo03 = random.randint(5, 10)
        cislo0_02 = random.randint(1, 10)
        cislo04 = random.randint(5, 20)
        print(" (", cislo01, "^",cislo0_01," + ", cislo02 , ") * (", cislo03, "^",cislo0_02,"+", cislo04, ") = ")
        a = int(input(" "))
        if a == (cislo01**cislo0_01 + cislo02)*(cislo03**cislo0_02+cislo04):
            print("Hooray!!! It's correct!"
                  "You're win at last level!!!"
                  "You very good at Math!")
            time.sleep(7)
            break
        else:
            print("Oops... It's not correct( You're at the 9 level")
            level -= 1